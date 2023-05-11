import json
import requests

from events.keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_pexels(city, state):
    # url = f"https://api.pexels.com/v1/search?query=city={city}&state={state}"
    header = {"Authorization": PEXELS_API_KEY}

    params = {"query": city + " " + state}
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params=params, headers=header)
    location = json.loads(response.content)

    photo = {"img_url": location["photos"][0]["src"]["original"]}
    return photo
