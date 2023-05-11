import json
import requests

from events.keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_pexels(city, state):
    header = {"Authorization": PEXELS_API_KEY}

    params = {"query": city + " " + state}
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params=params, headers=header)
    location = json.loads(response.content)

    photo = {"img_url": location["photos"][0]["src"]["original"]}
    return photo


def get_weather_data(city, state):
    # header = {"Authorization": OPEN_WEATHER_API_KEY}
    params = {
        "query": city
        + ", "
        + state
        + ", "
        + "USA&appid="
        + OPEN_WEATHER_API_KEY
    }

    url = "http://api.openweathermap.org/geo/1.0/direct"

    response = requests.get(url, params=params)
    location = json.loads(response.content)

    lat_lon = {"lat": location[0]["lat"]
               location[0]["lon"]}
    return lat, lon

    # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

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
