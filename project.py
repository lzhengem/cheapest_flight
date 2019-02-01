from flask import Flask, render_template, request,redirect, url_for
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


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        #get the parameters from form
        origin = request.form["origin"]
        destination = request.form["destination"]
        firstDepartureDate = request.form["firstDepartureDate"]
        lastDepartureDate = request.form["lastDepartureDate"]
        duration = request.form["duration"]
        nonStop = request.form["nonStop"]
        return redirect(url_for('flights',origin=origin,destination=destination,firstDepartureDate=firstDepartureDate,lastDepartureDate=lastDepartureDate,duration=duration,nonStop=nonStop))

    return render_template("homepage.html")

@app.route('/flights/<string:origin>/<string:destination>')
def flights(origin,destination):
    try:
        duration = request.args.get('duration')
        firstDepartureDate = request.args.get('firstDepartureDate')
        lastDepartureDate = request.args.get('lastDepartureDate')
        nonStop = request.args.get('nonStop')
        
        #request data from amadeus
        flights = amadeus.shopping.flight_dates.get(origin=origin, destination=destination, departureDate=departureDate,duration=duration,nonStop=nonStop).data
        # output = json.dumps(response)
        return render_template('flights.html',origin=origin,destination=destination,flights=flights)
    except ResponseError as error:
        output = "Response error"
        print(error)
    except Exception as error:
        output = "Exception error"
        print(error)
    return output

if __name__ == '__main__':
    app.debug = True    
    app.run(host='0.0.0.0', port = 8500)
