import phonenumbers
import opencage
import folium
from phonenumbers import number

# Extract country name

from phonenumbers import geocoder

# devide phone number into different subsections

pep.number = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
# Extract service provider name
print(carrier.name_from_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

key = "#opencagekey"

geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)
# print(results)

myMap = folium.Map(location = [lat, lng], zoom_start =_9)
folium.Marker([lat, lng], popup = location).add_to(myMap)

myMap.save("mylocation.html")