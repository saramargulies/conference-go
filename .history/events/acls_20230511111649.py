import json, requests

def get_pexels():
        url = "https://api.github.com/some/endpoint"
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.get(url, headers=header)