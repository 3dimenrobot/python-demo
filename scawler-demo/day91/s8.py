import  requests

requests.get(
    url='https:',
    verify=False, # 忽略证书
    # cert='fuck.pem'
    cert=('fuck.crt','xxx.key')
)

