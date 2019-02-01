from flask import Flask
import json

app = Flask(__name__)

AMADEUS_ID = json.loads(open('amadeus_client_secrets.json','r').read())['amadeus']['client_id']
AMADEUS_SECRET = json.loads(open('amadeus_client_secrets.json','r').read())['amadeus']['client_secret']


@app.route('/')
def home():
    return "Welcome to the homepage"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8500)
    app.debug = true