import  requests

post_dict = {
    'phone': '13552594619',
    'password': 'rbxh1949',
    'oneMonth': 1
}
response = requests.post(
    url='https://dig.chouti.com/login',
    data=post_dict
)

print(response.text)
cookie_dict = response.cookies.get_dict()
print(cookie_dict)