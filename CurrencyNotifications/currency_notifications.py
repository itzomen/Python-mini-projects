import requests, json, os
from datetime import date, datetime

#api to get currencies rates
URL = 'https://www.freeforexapi.com/api/live?pairs=USDEUR, USDGBP'

def get_latest_rates():
	day = date.today()
	#getting the json
	response = requests.get(URL)
	if response:
		print('Sucess!\n')
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
					print("Today's data Created, no change expected\n")
					return temp
				else:
					return temp
	else:
	   	with open('past_data.json', 'w') as file:
	   		json.dump(temp, file)
	   	print('Past Data Created, no change expected\n')
	   	return temp
	   	
def change_in_rates(dict):
	delta_rates = []
	with open('past_data.json') as f:
		past_data = json.load(f)
	del dict['day'], past_data['day']
	for pair, rates in dict.items():
		change = rates['rate']-past_data[pair]['rate']
		delta_rates.append([pair, round(change, 4)])
	return delta_rates

		
			
def main():
    rates = get_latest_rates()
    print(change_in_rates(rates))

if __name__ == '__main__':
    main()
