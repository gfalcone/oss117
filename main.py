from flask import Flask
from flask import request
from flask import Response
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    resp_data = {}
    resp_data['text'] = "<https://youtu.be/xGKowUNYrKA>"
    resp_data['token']= "5pwjbt39zj8i5dtux7jkaci4wc"
    
    resp = Response(content_type='application/json')
    resp.set_data(json.dumps(resp_data))

    return resp
