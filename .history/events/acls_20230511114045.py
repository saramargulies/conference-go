import json, requests


def get_pexels(city, state):
    payload = city, state
    url = "https://api.pexels.com/v1/search?query=" + payload
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.get(url, headers=header)
    location = json.loads(response.content)
    return location



print(get_pexels())