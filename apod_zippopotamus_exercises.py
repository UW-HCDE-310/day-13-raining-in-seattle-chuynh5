import urllib.request
import json


# Exercise 1: Get APODs between two dates
def get_apods_between(api_key, start_date, end_date):

    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}"

    with urllib.request.urlopen(url) as request:
        response = json.load(request)

    apod_titles = [item['title'] for item in response]
    return apod_titles


# Test for Exercise 1
apod_titles = get_apods_between("DEMO_KEY", "2023-01-01", "2023-01-07")
print("APOD Titles:", apod_titles)


# Exercise 2a: Get info about a specific zip code
def zipcode_info(countrycode, zipcode):

    url = f"https://api.zippopotam.us/{countrycode}/{zipcode}"
    try:
        with urllib.request.urlopen(url) as request:
            data = json.load(request)
            return data
    except Exception as e:
        print("Error:", e)
        return None


# Test for Exercise 2a
zip_data = zipcode_info("US", "98105")
print("Zip Code Data:", zip_data)


# Exercise 2b: Simplified Place class and parsing
class Place:


    def __init__(self, name, state, latitude, longitude):
        self.name = name
        self.state = state
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"{self.name}, {self.state} (Lat: {self.latitude}, Lon: {self.longitude})"


def get_places_from_zip(zip_data):

    if not zip_data or "places" not in zip_data:
        return []

    places = [
        Place(
            place["place name"],
            place["state"],
            place["latitude"],
            place["longitude"]
        )
        for place in zip_data["places"]
    ]

    return places


# Test for Exercise 2b
places = get_places_from_zip(zipcode_info("US", "02861"))
print("Places:", places)
