# Description

Attempting to run code from README (https://github.com/amadeus4dev/amadeus-python) fails

# Steps to Reproduce
1. Run
```
from amadeus import Client, ResponseError

amadeus = Client(
    client_id=AMADEUS_ID,
    client_secret=AMADEUS_SECRET
)

try:
    response = amadeus.shopping.flight_dates.get(origin='NYC', destination='MAD')
    print(response.data)
except ResponseError as error:
    print(error)
except Exception as e:
    print(e)
```


## Expected Behavior:
To get a response object

## Actual Bahavior:
```HTTP Error 404: Not Found```

## Stable Behavior? [What percentage of the time does it reproduce?]
Right now it is stable, 100% reproducibility.

# Versions
Python: python2.7

Pip: pip 19.0.1

# Checklist
Please make sure you checked the following:

Are you running Python 2.7 or 3.6? Yes

Did you download the latest version of this package? Yes