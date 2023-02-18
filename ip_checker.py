import requests
def ip_check():
	url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
	querystring = {"ip":ip}

	headers = {
		"X-RapidAPI-Key": "1541f0121dmsh0e632ec08e4880dp17fb12jsnf92fe854c822",
		"X-RapidAPI-Host": "ip-geolocation-ipwhois-io.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	#print(response.text)
	data = {'ip', 'success', 'type', 'continent', 'country', 'country_code', 'country_flag', 'country_capital', 'country_neighbours', 'region', 'city', 'latitude', 'longitude', 'asn', 'org', 'isp', 'timezone', 'timezone_name', 'timezone_dstOffset', 'timezone_gmtOffset', 'timezone_gmt', 'currency', 'currency_code', 'currency_symbol', 'currency_rates', 'currency_plural', 'completed_requests'}

	if response.json()['success'] == False:
		print("Invalid IP Address")
	else:
		print('RESULTS')
		for item in data:
			value = str(response.json()[item])
			if value == None:
				value = 'N/A'
			else:
				value = value
			print(f"{item}: {value}")

ip = input("Enter IP Address: ")
ip_check()