from flask import Flask, render_template, request,redirect, url_for
import json
import requests
from datetime import datetime, timedelta
from functools import reduce
from amadeus import Client, ResponseError

import os #so that we can listen on the environment port
app = Flask(__name__)

#check to see if app is being deployed on Heroku or local
ON_HEROKU = False
debug = True
if 'DYNO' in os.environ:
    ON_HEROKU = True
    debug = False

# AMADEUS_ID = json.loads(open('amadeus_client_secrets.json','r').read())['amadeus']['client_id']
# AMADEUS_SECRET = json.loads(open('amadeus_client_secrets.json','r').read())['amadeus']['client_secret']
AMADEUS_ID = os.environ.get('AMADEUS_ID')
AMADEUS_SECRET = os.environ.get('AMADEUS_SECRET')

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
        #convert strings to dates
        firstDate = datetime.strptime(firstDepartureDate, '%Y-%m-%d')
        lastDate = datetime.strptime(lastDepartureDate, '%Y-%m-%d')
        
        #get a list of all the dates from firstDate to lastDate
        allDepartureDates = [str((firstDate + timedelta(days=x)).date()) for x in range(0, (lastDate-firstDate).days + 1)]
        
        #for each departure date, request data from amadeus and collect them into flights
        flights = reduce(lambda x, departureDate : x + amadeus.shopping.flight_dates.get(origin=origin, destination=destination, departureDate=departureDate,duration=duration,nonStop=nonStop).data, allDepartureDates, [])
        return render_template('flights.html',origin=origin,destination=destination,flights=flights)
        
    except ResponseError as error:
        output = "Response error"
        print(error)
    except Exception as error:
        output = "Exception error"
        print(error)
    return output

if __name__ == '__main__':
    app.debug = debug
    port = int(os.environ.get('PORT',8500))
    app.run(host='0.0.0.0', port = port)
    # app.run()
