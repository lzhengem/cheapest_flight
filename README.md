# Introduction
cheapest_flight is an app in which you can enter a origin and destination, with a duration and time frame and it will return the cheapest flight. (Still in progress)

## Installation
1. python2.7

2. flask

3. amadeus - You will need a client id and client secret from https://developers.amadeus.com/self-service/category/203/api-doc/5/api-docs-and-example/10003
* save the client id and client secret in a file called "amadeus_client_secrets.json" in the same folder as project.py
* it should look like this:
```
{"amadeus":
    {"client_id": "yourclientid",
    "client_secret": "yourclientsecret"}

}
```

## Usage
1. Run the project
```python project.py```
2. Go on your web browser to http://localhost:8500

## Description
* Enter in origin
* Enter in destination
* Enter in departure date
* Enter duration of trip
* Choose nonStop or any
* After submitting the form, it will give you the cheapest dates to fly for the choosen dates


