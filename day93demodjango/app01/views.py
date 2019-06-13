from django.shortcuts import render,HttpResponse

# Create your views here.
import requests
import time
import re
CTIME = None
QCODE = None
TIP = 1
TICKET_DICT = {}
USER_INIT_DICT = {}
ALL_COOKIE_DICT = {}


def login(req):
    global  CTIME
    CTIME = time.time()
    resp = requests.get(
        url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&fun=new&lang=zh_CN&_=%s" % CTIME,
    )
    print(resp.text) # window.QRLogin.code = 200; window.QRLogin.uuid = "Qdf1sTuGaQ==";
    v = re.findall('uuid = "(.*)"',resp.text)
    global  QCODE
    QCODE = v[0]
    return render(req,'login.html',{'qcode':QCODE})

import json
def checkLogin(req):
    """
    监听用户是否已经扫码
    监听用户是否已经点击确认
    :param request:
    :return:
    """
    global TIP
    ret = {'code': 408,'data': None}
    r1 = requests.get(
        url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=%s&tip=%s&r=95982085&_=%s" %(QCODE,TIP,CTIME,)
    )
    if 'window.code=408' in  r1.text:
        print('无人扫码')
        return HttpResponse(json.dumps(ret))
    elif 'window.code=201' in  r1.text:
        ret['code'] = 201
        avatar = re.findall("window.userAvatar = '(.*)';", r1.text)[0]
        ret['data'] = avatar
        TIP = 0
        return HttpResponse(json.dumps(ret))
    elif 'window.code=200' in  r1.text:
        # 用户点击确认登录，
        """
        window.code=200;
        window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AYKeKS9YQnNcteZCfLeTlzv7@qrticket_0&uuid=QZA2_kDzdw==&lang=zh_CN&scan=1494553432";
        window.redirect_uri="https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AYKeKS9YQnNcteZCfLeTlzv7@qrticket_0&uuid=QZA2_kDzdw==&lang=zh_CN&scan=1494553432";
        """
        ALL_COOKIE_DICT.update(r1.cookies.get_dict())

        redirect_uri = re.findall('window.redirect_uri="(.*)";', r1.text)[0]
        redirect_uri = redirect_uri + "&fun=new&version=v2"

        # 获取凭证
        r2 = requests.get(url=redirect_uri)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r2.text,'html.parser')
        for tag in soup.find('error').children:
            TICKET_DICT[tag.name] = tag.get_text()
        ALL_COOKIE_DICT.update(r2.cookies.get_dict())
        print("TICKET_DICT",TICKET_DICT)
        ret['code'] = 200
        return HttpResponse(json.dumps(ret))




def user(request):
    """
    个人主页
    :param request:
    :return:
    """
    # 获取用户信息
    # https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=88828930&lang=zh_CN&pass_ticket=uBfBw5um5Zor97ihMqdFprf4kqjecz8q0VRdevL%252BMg7Ozij4NvnpZCevYQX5jhO0
    get_user_info_data = {
        'BaseRequest': {
            'DeviceID': "e402310790089148",
            'Sid':TICKET_DICT['wxsid'],
            'Uin':TICKET_DICT['wxuin'],
            'Skey':TICKET_DICT['skey'],
        }
    }
    get_user_info_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=88828930&lang=zh_CN&pass_ticket=" +TICKET_DICT['pass_ticket']
    r3 = requests.post(
        url=get_user_info_url,
        json=get_user_info_data
    )
    r3.encoding = 'utf-8'
    user_init_dict = json.loads(r3.text)
    ALL_COOKIE_DICT.update(r3.cookies.get_dict())
    # global USER_INIT_DICT
    # USER_INIT_DICT = user_init_dict
    print("user_init_dict", user_init_dict)
    USER_INIT_DICT.update(user_init_dict)
    return render(request,'user.html',{'user_init_dict':user_init_dict})

def contact_list(request):
    """
    获取所有联系人,并在页面中显示
    :param request:
    :return:
    """
    # https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket=J6GLa%252FBobIDCebI4llpykyMrbHPm86KGMDqE4jUS20OCwWhkK%252BF6uiJpLM%252BO5PoU&r=1494811126614&seq=0&skey=@crypt_d83b5b90_eb1965b01a3bc3f4d7a4bdc846b77a19
    ctime = str(time.time())
    base_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket=%s&r=%s&seq=0&skey=%s"
    url = base_url %(TICKET_DICT['pass_ticket'],ctime,TICKET_DICT['skey'])
    response = requests.get(url = url,cookies=ALL_COOKIE_DICT)
    response.encoding = 'utf-8'
    contact_list_dict = json.loads(response.text)
    for item in contact_list_dict['MemberList']:
        print(item['NickName'],item['UserName'])
    print("contact_list_dict",contact_list_dict)
    return render(request,'contact_list.html',{'contact_list_dict':contact_list_dict})

