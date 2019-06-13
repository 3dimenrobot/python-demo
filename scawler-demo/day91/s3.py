import requests

resp = requests.post(
    url='https://dig.chouti.com/link/vote?linksId=26485946',
    cookies={
        'gpsd':'648ce6684e5f97799db4e1d503978667'
    }
)


print(resp.text)