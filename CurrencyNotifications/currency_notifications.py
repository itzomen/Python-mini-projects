import requests, json, os, time
from datetime import date, datetime

#api to get currencies rates
URL = 'https://www.freeforexapi.com/api/live?pairs=USDEUR, USDGBP'
IFTTT_URL = 'https://maker.ifttt.com/trigger/{}/with/key/{ your key }'

def get_latest_rates():
	day = date.today()
	#getting the json
	response = requests.get(URL)
	if response:
		print('Sucess getting rates!\n')
	else:
		print('Error getting Rates')
	new_data = response.json()
	temp = new_data['rates']
	temp['day'] = str(day)
	
	if os.path.isfile('./past_data.json'):
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
	delta_rates = {}
	with open('past_data.json') as f:
		past_data = json.load(f)
	del dict['day'], past_data['day']
	for pair, rates in dict.items():
		change = rates['rate']-past_data[pair]['rate']
		delta_rates[pair] = round(change, 4)
	return delta_rates


def post_to_webhook(event, value):
    #data that will be sent to IFTTT service
    data = {'value1': value}
    # inserts event name into IFTTT URL
    event_url = IFTTT_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(event_url, json=data)
    
def format_data(rate_dict, delta_dict):
 	lines = []
 	for pair, rates in rate_dict.items():
 		current = rates['rate']
 		delta = delta_dict[pair]
 		line = '{} Rate: <b>{}</b> Change <i>{}</i>'.format(pair, current, delta)
 		lines.append(line)
 	return '<br>'.join(lines)

			
def main():
    posts = []
    print('Running......')
    while True:
    	rates = get_latest_rates()  
    	deltas = change_in_rates(rates)
    	posts.append(format_data(rates, deltas))
    	# send updates
    	if len(posts)== 3:
    		all_posts = '<br>'.join(posts)
                #'daily_currency_rates' is the event name I created from the IFTTT app
    		post_to_webhook('daily_currency_rates', all_posts)
    		print("\nDaily Update Sent")
    		posts = []
    	# program remains inactive
    	time.sleep(30)

if __name__ == '__main__':
    main()
