import json
import requests

from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_pexels(city, state):
    header = {"Authorization": PEXELS_API_KEY}

    params = {"query": city + " " + state}
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params=params, headers=header)
    location = json.loads(response.content)

    photo = {"img_url": location["photos"][0]["src"]["original"]}
    return photo


def get_lat_lon(location):
    params = {
        "q": f"{location.city},{location.state.abbreviation},USA",
        "appid=": OPEN_WEATHER_API_KEY,
    }

    url = "http://api.openweathermap.org/geo/1.0/direct"
    print("this is my params:", params)
    response = requests.get(url, params=params)
    print("this is the response:", response)
    parsed_json = json.loads(response.content)
    print(parsed_json)

    lat_lon = {"lat": parsed_json[0]["lat"], "lon": parsed_json[0]["lon"]}
    return lat_lon


def get_weather_data(location):
    lat_long = get_lat_lon(location)
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat_long["lat"],
        "lon": lat_long["lon"],
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    response = requests.get(url, params=params)
    parsed_json = json.loads(response.content)

    weather = {
        "temp": parsed_json["main"]["temp"],
        "description": parsed_json["weather"][0]["description"],
    }
    return weather


# Create the URL for the geocoding API with the city and state
# Make the request
# Parse the JSON response
# Get the latitude and longitude from the response

# Create the URL for the current weather API with the latitude
#   and longitude
# Make the request
# Parse the JSON response
# Get the main temperature and the weather's description and put
#   them in a dictionary
# Return the dictionary
