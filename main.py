import requests
url = 'http://localhost:3000/sample.php'
obj = {'username':'Usf', 'password':'123456'}

res = requests.post(url, data = obj)
print(res.text)