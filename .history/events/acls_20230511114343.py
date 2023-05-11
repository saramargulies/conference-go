import json, requests


def get_pexels(city, state):
    payload = {"city": city, "state": state}
    url = "https://api.pexels.com/v1/search?query="
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.get(url, headers=header, pa)
    location = json.loads(response.content)
    return location


a = "Atlanta"
s = "Georgia"

print(get_pexels(a, s))
