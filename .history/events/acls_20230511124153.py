import json, requests


def get_pexels(city, state):
    url = f"https://api.pexels.com/v1/search?query={city}&per_page=1"
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.post(url, headers=header)
    location = json.loads(response.content)

    location

    return 


a = "Atlanta"
s = "Georgia"

print(get_pexels(a, s))
