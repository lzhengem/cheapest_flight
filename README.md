# Introduction
cheapest_flight is an app in which you can enter a origin and destination, with a duration and time frame and it will return the cheapest flight. (Still in progress)

## Installation
You can check this project out at: http://cheapest-flight.herokuapp.com

Or if you would like to install it yourself:
1. python2.7

2. flask

3. amadeus - You will need a client id and client secret from https://developers.amadeus.com/self-service/category/203/api-doc/5/api-docs-and-example/10003

4. Set up your environment variable AMADEUS_ID and AMADEUS_SECRET:
```
AMADEUS_ID={YOUR ID}
AMADEUS_SECRET={YOUR SECRET}
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

## Backstory
Me and my friends had wanted to go to Japan in the month of August. We didn't really care when we left, as long as it was in August and it lasted for 2 weeks. We wanted to find the cheapest dates to go. It would have been very cumbersome to lookup each day in the month of August manually to find the cheapest flights, so this app was born!
