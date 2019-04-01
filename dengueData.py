from flask import Flask, request
import SocialMedia_API

app = Flask(__name__)
socialMedia = SocialMedia_API.SocialMedia()

@app.route('/',methods=['GET'])
def verify():
    return str(socialMedia.get_dengue_data()).replace("'",'"')
