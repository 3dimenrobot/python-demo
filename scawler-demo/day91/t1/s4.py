import requests

# 程序不成功，可能是有安全设置，与老师讲解的不同。
r1 = requests.get('https://github.com/')
# print(r1)
print(r1.cookies.get_dict())
# r1_cookies = r1.cookies.get_dict();
#
# post_dict = {
#     'phone': '13552594619',
#     'password': 'rbxh1949',
#     'oneMonth': 1
# }
# r2 = requests.post(
#     url='https://dig.chouti.com/login',
#     data=post_dict
# )
#
# r2_cookies = r2.cookies.get_dict();
# print(r2_cookies)
#
#
# r3 = requests.post(
#     url='https://dig.chouti.com/link/vote?linksId=26485946',
#     cookies={
#         # 'gpsd':r2_cookies['gpsd']
#         'gpsd':r1_cookies['gpsd']
#     }
# )
#
#
# print(r3.text)