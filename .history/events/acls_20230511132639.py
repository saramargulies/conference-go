import json, requests
# from .keys import PEXELS_API_KEY


def get_pexels(city, state):
    url = f"https://api.pexels.com/v1/search?query=city={city}&state={state}"
    header = {"Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"}
    response = requests.post(url, headers=header)
    location = json.loads(response.content)

    params={
        "query": city + " " + state
    }

    print(response.text)
    # location_dict = {
    #     "img_url" = location[""]
    # }
    return location


a = "Atlanta"
s = "Georgia"

print(get_pexels(a, s))
