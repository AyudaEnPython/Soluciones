"""
Calling a Json API

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geojson.py. The program will prompt for a
location, contact a web service and retrieve JSON for the web service
and parse that data, and retrieve the first place_id from the JSON. A
place ID is a textual identifier that uniquely identifies a place as
within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has
a static subset of the Google Data:

    http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API
also has no rate limit so you can test as often as you like. If you
visit the URL with no parameters, you get "No address..." response.

To call the API, you need to include a key= parameter and provide the
address that you are requesting as the address= parameter that is
properly URL encoded using the urllib.parse.urlencode() function as
shown in http://www.py4e.com/code3/geojson.py

Test Data / Sample Execution

You can test to see if your program is working with a location of
"South Federal University" which will have a place_id of
"ChIJLzabHQ7i2IgRzeZb_AgUj0Q".

    +------------------------------------------+
    | $ python3 solution.py                    |
    | Enter location: South Federal University |
    | Retrieving http://...                    |
    | Retrieved 2146 characters                |
    | Place id ChIJLzabHQ7i2IgRzeZb_AgUj0Q     |
    +------------------------------------------+

Turn In

Please run your program to find the place_id for this location:

    +-----------------------------+
    | University of Texas         |
    +-----------------------------+

Make sure to enter the name and case exactly as above and enter the
place_id and your Python code below. Hint: The first seven characters
of the place_id are "ChIJt8- ..."

Make sure to retreive the data from the URL specified above and not the
normal Google API. Your program should work with the Google API - but
the place_id may not match for this assignment.
"""
import urllib.request
import json
import ssl

SERVICE_URL = "http://py4e-data.dr-chuck.net/json?"
LOCATION = "University of Texas"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

params = {}
params['address'] = LOCATION
params['key'] = 42

url = SERVICE_URL + urllib.parse.urlencode(params)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

print("Enter location:", LOCATION)
print("Retrieving", url)
print("Retrieved", len(data), "characters")  # 1646

js = json.loads(data)

print(js['results'][0]['place_id'])  # ChIJt8-EJZu1RIYR3iFKF0_uMYE
