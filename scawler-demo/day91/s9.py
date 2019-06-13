import requests

session = requests.Session()

### 1、首先登陆任何页面，获取cookie

i1 = session.get(url="http://dig.chouti.com/help/service")

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = session.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "8615131255089",
        'password': "xxxxxx",
        'oneMonth': ""
    }
)

i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=8589623",
)
print(i3.text)