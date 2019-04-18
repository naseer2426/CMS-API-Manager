import json
import urllib.request as ur
import pprint
import pyrebase

class HazeAPI:
    def __init__(self):
        config = {
          "apiKey": "",
          "authDomain": "",
          "databaseURL": "https://data-storage-1205f.firebaseio.com/",
          "storageBucket": ""
        }
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def getJSON(self):
        url = "https://api.data.gov.sg/v1/environment/psi"
        url_parser = ur.urlopen(ur.Request(url))
        json_object = url_parser.read()
        json_dict = json.loads(json_object.decode('utf-8'))
        air_status = json_dict['api_info']['status']
        timestamp = json_dict['items'][0]['update_timestamp']
        psi_readings = json_dict['items'][0]['readings']['psi_twenty_four_hourly']
        pm25 = json_dict['items'][0]['readings']['pm25_twenty_four_hourly']
        location = {}
        json_returner = {}
        for item in json_dict['region_metadata']:
            location[item['name']] = item['label_location']
        json_returner['air_status'] = air_status
        json_returner['timestamp'] = timestamp
        json_returner['psi'] = psi_readings
        json_returner['pm25'] = pm25
        json_returner['location'] = location
        return json_returner
    
    def getJSONHazeRange(self,old_datetime):
        #old_datetime = Y\YYY-MM-DD
        old_date_url = "https://api.data.gov.sg/v1/environment/psi?"+"date="+old_datetime
        url_parser = ur.urlopen(ur.Request(old_date_url))
        json_object = url_parser.read()
        json_dict = json.loads(json_object.decode('utf-8'))
        air_status = json_dict['api_info']['status']
        timestamp = json_dict['items'][0]['update_timestamp']
        psi_readings = json_dict['items'][0]['readings']['psi_twenty_four_hourly']
        pm25 = json_dict['items'][0]['readings']['pm25_twenty_four_hourly']
        location = {}
        json_returner = {}
        for item in json_dict['region_metadata']:
            location[item['name']] = item['label_location']
        json_returner['air_status'] = air_status
        json_returner['timestamp'] = timestamp
        json_returner['psi'] = psi_readings
        json_returner['pm25'] = pm25
        json_returner['location'] = location
        return json_returner

    def write_firebase(self):
        data = self.getJSON()
        self.db.child("Haze_Data").set(data)

if __name__ == '__main__':
    h = HazeAPI()
    h.write_firebase()
