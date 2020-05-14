import requests
import json


class Get_data():
    def __init__(self):
        self.india_today_count = {}
        self.maharashtra_today_count = {}
        self.pune_today_count = {}

    def get_data(self):
        india_url = "https://api.covid19india.org/data.json"
        pune_url = 'https://api.covid19india.org/state_district_wise.json'
        payload = {}
        headers= {}

        try:
            india_response = requests.request("GET", india_url, headers = headers, data = payload)
            pune_response = requests.request("GET", pune_url, headers = headers, data = payload)
        except requests.exceptions.RequestException as e:
            with open("log.txt", 'a') as log:
                print(e)
                log.write(str(e))
            return 
        except :
            with open("log.txt", 'a') as log:
                print("Error : in get_data")
                log.write("Error : in get_data")
            return 

        india_data = india_response.text
        pune_data = pune_response.text
        india_parsed = json.loads(india_data)
        pune_parsed = json.loads(pune_data)

        self.india_today_count = india_parsed['cases_time_series'][-1]
        self.maharashtra_today_count = india_parsed['statewise'][1]
        self.pune_today_count = pune_parsed['Maharashtra']['districtData']['Pune']

        return

