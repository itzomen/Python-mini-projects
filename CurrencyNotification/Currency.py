import requests

URL = 'https://api.exchangeratesapi.io/latest?base=USD'
response = requests.get(URL)
if response:
    print('Success!')
else:
    print('An error has occurred.')

#print(type(r))
#print(r.content)
data = response.json()
print(data)
