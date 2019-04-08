import requests
import json
import pprint

class CDShelter:
    def __init__(self,email = "cmshelp10@gmail.com",password = "ThisIsSuperSAD"):
        self.email = email
        self.password = password
        self.request_url = 'https://developers.onemap.sg/privateapi/themesvc/retrieveTheme?queryName=civildefencepublicshelters&token='
        self.access_token = ''

    def get_access_token(self):
        url = "https://developers.onemap.sg/privateapi/auth/post/getToken"

        payload = "{\"email\":\"cmshelp10@gmail.com\", \"password\":\"ThisIsSuperSAD\"}"
        headers = {
            'accept': "application/json",
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "e3b063c2-a38d-49b6-b07a-04f11fd23670"
            }
        response = requests.request("POST", url, data=payload, headers=headers).json()

        self.access_token = response['access_token']

    def get_cd_shelter_locations(self):
        self.get_access_token()
        #print(self.request_url + self.access_token)

        #response = requests.get(self.request_url + self.access_token).json()
        url = "https://developers.onemap.sg/privateapi/themesvc/retrieveTheme"

        querystring = {"queryName":"civildefencepublicshelters","token":self.access_token}

        headers = {
            'accept': "application/json",
            'Content-Type': "application/json"
            }
        response = requests.request("GET", url, params=querystring, headers=headers).json()

        results = response['SrchResults'][1:]

        cd_shelter_list = []

        for result in results:
            latlng = result['LatLng'].split(',')
            cd_shelter_list.append({
                                    'lat':latlng[0],
                                    'lng':latlng[1]})

        return cd_shelter_list

    def write_json_file(self,title):
        try:
            with open(title, 'w') as json_file:
                json.dump(self.get_cd_shelter_locations(), json_file)
            return 'Json file saved successfully'
        except:
            return 'Json file not saved, an error has occurred'

# cd_shelter_list = CDShelter().get_cd_shelter_locations()

# write_result = CDShelter().write_json_file('Civil defence shelter locations')

# pp = pprint.PrettyPrinter()
# pp.pprint(write_result)
# pprint.pprint(cd_shelter_list)
