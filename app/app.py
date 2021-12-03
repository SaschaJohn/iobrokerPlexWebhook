from flask import Flask,request,json
import json
import requests
import sys
import os

iobrokerState = os.environ['IOBROKER_STATE_URL']
app = Flask(__name__)

@app.route('/')
def index():
    return 'Webhooks with Python'

@app.route('/plex', methods=['POST'])
def plex():
  data = json.loads(request.form['payload'])
  print(data['event'], file=sys.stderr)
  print(iobrokerState, file=sys.stderr)
  url=str(iobrokerState)+str(data) 
  requests.get(url)
  return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
