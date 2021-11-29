from flask import Flask,request,json
import json
import requests
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return 'Webhooks with Python'

@app.route('/plex', methods=['POST'])
def plex():
  data = json.loads(request.form['payload'])
  print(data['event'], file=sys.stderr)
  requests.get('http://192.168.178.145:8087/set/0_userdata.0.plexEvent?value='+data)
  return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
