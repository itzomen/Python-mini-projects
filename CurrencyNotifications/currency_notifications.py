import requests, json
from datetime import date

#api to get currencies rates
URL = 'https://www.freeforexapi.com/api/live?pairs=USDEUR, USDGBP'

def get_latest_rates():
	day = date.today()
	#getting the json
	response = requests.get(URL)
	if response:
		print('Sucess!')
	else:
		print('Error getting Rates')
	new_data = response.json()
  #  with open('past_data.json', 'w') as file:
    #	json.dump(new_data['rates'], file)
