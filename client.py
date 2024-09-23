
import requests

url = 'http://localhost:8555/' 
data = {'value': ''}
response = requests.get(url, params=data)  
response = response.json()
print(response)
