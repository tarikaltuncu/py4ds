import requests

# Download the JSON data from OpenNotify.org's iss-now.json API.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)

# Assign the JSON data to a variable.
data = response.json()
print(data)

# Print the latitude and longitude of the ISS.
print(data['iss_position']['latitude'])
print(data['iss_position']['longitude'])

from c10_objects import Point
iss_position = Point(float(data['iss_position']['latitude']), float(data['iss_position']['longitude']))
print(iss_position)