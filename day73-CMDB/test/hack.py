import requests

import  hashlib
import time
cur_time = time.time()
app_id="abcdefghij"
app_id_time='%s|%s' %(app_id,cur_time)
m=hashlib.md5()
m.update(bytes(app_id_time,encoding='utf-8'))
authkey=m.hexdigest()

authkey_time='%s|%s' %(authkey,cur_time)
print(authkey_time)
host_data = {
    'status':True,
    'data':{
        'hostname':'c1.com',
        'disk':{'status':True,'data':'xxx'},
        'mem':{'status':True,'data':'xxx'},
        'nic':{'status':True,'data':'xxx'},
    }
}


# requests.get(url='http://127.0.0.1:8000/api/asset/?K1=123')
# requests.get(url='http://127.0.0.1:8000/api/asset/',params={'K1':'V1',"k2":'V2'})

# requests.post(url='http://127.0.0.1:8000/api/asset/',params={'K1':'V1',"k2":'V2'})
# requests.post(url='http://127.0.0.1:8000/api/asset/',
#               params={'K1':'V1',"k2":'V2'},  # GET 传值
#               data={'username':'123',"pwd":'333',},  # POST 传值
#               headers={'a':'aaa'} # 请求头数据
# )

response = requests.post(url='http://127.0.0.1:8000/api/asset/',
              # data=host_data,  # POST 传值
              json=host_data,
             # http 请求头不能加_
              headers={'authkey':"87425135893e74f1d597fef39aa30694|1558103686.5206637"}
)

print(response.text)

# requests.get(url='http://127.0.0.1:8000/api/asset/')