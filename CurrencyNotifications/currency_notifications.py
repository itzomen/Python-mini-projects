import requests, json

#api to get currencies rates
URL = 'https://www.freeforexapi.com/api/live?pairs=USDEUR'

#getting the json
response = requests.get(URL)
if response:
    print('Success!')
else:
    print('An error has occurred.')

#saving fetched json into dictionary
new_data = response.json()

#saving new_data in json file
with open('past_data.json', 'w') as file:
	json.dump(new_data['rates'], file)
