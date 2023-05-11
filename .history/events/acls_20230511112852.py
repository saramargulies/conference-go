import json, requests


def get_pexels():
    payload = {loca: 'value1', 'key2': 'value2'}
    url = "https://api.pexels.com/v1/search?query=city"
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.get(url, headers=header)
    location = json.loads(response.content)
    return location


print(get_pexels())
