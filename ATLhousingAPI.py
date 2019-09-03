from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/all')
def retrieveData():
	headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJ1c2VyX2lkIjo0LCJleHAiOjE1Nzc4MzY4MDB9.h5wCxPgv6lJmsVssaG50WUh63PxyR4va0Rgf0x48c_M'}

	res = requests.get('http://houseatl.cloud.rnoc.gatech.edu/rest/properties?select=*,owners(*)', headers = headers).content
	print(res)
	return res

if __name__ == '__main__':
	app.run()
