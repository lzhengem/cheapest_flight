from flask import Flask, render_template
import json
import requests
from amadeus import Client, ResponseError

app = Flask(__name__)

AMADEUS_ID = json.loads(open('amadeus_client_secrets.json','r').read())['amadeus']['client_id']
AMADEUS_SECRET = json.loads(open('amadeus_client_secrets.json','r').read())['amadeus']['client_secret']

amadeus = Client(
    client_id=AMADEUS_ID,
    client_secret=AMADEUS_SECRET
)


@app.route('/')
def home():
    return render_template("homepage.html")
  
if __name__ == '__main__':
    app.debug = True    
    app.run(host='0.0.0.0', port = 8500)
