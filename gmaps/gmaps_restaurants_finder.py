import googlemaps
from datetime import datetime
import json
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyDAOpH3KzlnMy45taoxIKMvDj23q4uneTI')

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
places_result = gmaps.places('places to eat near me',
                             location=(-33.865586,151.205439),
                             radius=400,
                             open_now=True
                             )
#print(json.dumps(places_result,indent=4))
results = places_result['results']
place_data = [
    {
        'formatted_address':p['formatted_address'],
        'name':p['name'],
        'place_id':p['place_id'],
        'rating':p['rating'],
        'types':p['types']
    } for p in results]
