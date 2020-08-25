import requests, json, os
from datetime import date, datetime

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
	temp = new_data['rates']
	temp['day'] = str(day)
	
	if os.path.isfile('./past_data.json'):
			#TODO: open past_data.json and verify if created on the same day
			with open('past_data.json') as file:
				data = json.load(file)
				date_created = datetime.strptime(data['day'] , '%Y-%m-%d').date()
				if date_created != day:
					with open('past_data.json', 'w') as file:
						json.dump(temp, file)
					return temp
	else:
	   	with open('past_data.json', 'w') as file:
	   		json.dump(temp, file)
	   	return temp
	
def main():
    rates = get_latest_rates()

if __name__ == '__main__':
    main()
