import requests

url = 'http://192.168.0.183:8000/apitest'

data = {'token':'abc1234'}
r = requests.get(url=url,data=data)
print(r.status_code)

print(r.json())