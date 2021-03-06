import random

from flask import Flask
from flask import request
from flask import Response

import json

VIDEO_LINKS = [
	'https://www.youtube.com/watch?v=xGKowUNYrKA',
	'https://www.youtube.com/watch?v=s6ylqpyik9M',
	'https://www.youtube.com/watch?v=wx2m0mOQ37w',
	'https://www.youtube.com/watch?v=H7cAkkz0gEI',
	'https://www.youtube.com/watch?v=gpcVS9lyiMg',
	'https://www.youtube.com/watch?v=JnqczbKNrVo',
	'https://www.youtube.com/watch?v=_F1QkeAT0Cw',
	'https://www.youtube.com/watch?v=OCxAITH-Jcw',
	'https://www.youtube.com/watch?v=Nd-17LsIMUo',
	'https://www.youtube.com/watch?v=zGYxYMJQCmM',
	'https://www.youtube.com/watch?v=FzUxqmQuE5c',
	'https://www.youtube.com/watch?v=U5hNe9tt67Q',
	'https://www.youtube.com/watch?v=ghTsp78-UnA',
	'https://www.youtube.com/watch?v=1nuddvBaH2k',
	'https://www.youtube.com/watch?v=5L6e8tO9I4c',
	'https://www.youtube.com/watch?v=sRc1KvuTUQk',
	'https://www.youtube.com/watch?v=oe9z8_EZGjY',
	'https://www.youtube.com/watch?v=VpbhmR171N0',
	'https://www.youtube.com/watch?v=mBB4JBRjYVU',
	'https://www.youtube.com/watch?v=64QjwYDaSEw',
	'https://www.youtube.com/watch?v=S2qLOg-de0o',
	'https://www.youtube.com/watch?v=TgJM5Lnkgh8'
]

ICON_URL = 'https://static-s.aa-cdn.net/img/gp/20600007231143/U6Pbz5rbmBOvy5nIWsjLAnQal_lGXJ0uzbpN1Ta9Rgd4DKequUFBDC-yNyAVgYUijbHq=w300?v=1' # NOQA

TOKEN = '5pwjbt39zj8i5dtux7jkaci4wc'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():

	resp_data = {}
	resp_data['text'] = '''OSS 117, pour vous servir
{}'''.format(random.choice(VIDEO_LINKS))
	resp_data['icon_url'] = ICON_URL
	resp_data['response_type'] = 'in_channel'
	resp_data['token'] = TOKEN

	resp = Response(content_type='application/json')
	resp.set_data(json.dumps(resp_data))
	return resp
