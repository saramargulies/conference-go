import json, requests

def get_pexels():
    url = "https://api.pexels.com"
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.get(url, headers=header)
    location = json.loads(response.content)
    location_dict = 