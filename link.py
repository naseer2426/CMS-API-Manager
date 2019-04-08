from flask import Flask, request
import SocialMedia_API
from CD_Shelter import CD_Shelter_API

app = Flask(__name__)
socialMedia = SocialMedia_API.SocialMedia()
cd = CD_Shelter_API.CDShelter()

@app.route('/',methods=['GET'])
def verify():
    # json_data = {}
    json_data = socialMedia.get_dengue_data()
    json_data['data_cdshelter'] = cd.get_cd_shelter_locations()
    json_data['data_haze'] = socialMedia.API.getHaze()
    json_data['CD_data'] = socialMedia.API.getCDShelterData()
    return str(json_data).replace("'",'"')
