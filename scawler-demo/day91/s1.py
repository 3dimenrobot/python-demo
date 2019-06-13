import requests

from bs4 import  BeautifulSoup
response = requests.get('http://www.autohome.com.cn/news/')

response.encoding = response.apparent_encoding


soup = BeautifulSoup(response.text,features='html.parser')


target = soup.find(id='auto-channel-lazyload-article')

list_list = target.find_all('li')

for i in list_list:
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        h3 = a.find('h3') # 对象类型
        print(h3.text,type(h3))
        imgsrc = a.find('img').attrs.get('src')
        print(imgsrc)
        # 保存图片
        imgsrc = 'https:' + imgsrc
        imgresp = requests.get(url=imgsrc)

        import uuid
        file_name = 'img/' + str(uuid.uuid4())+".jpg"
        with open(file_name,'wb') as f:
            f.write(imgresp.content)