import json, requests
from .keys import PEXELS_API_KEY


def get_pexels(city, state):
    url = f"https://api.pexels.com/v1/search?query=city={city}&state=Colorado"
    header = {"Authorization": PEXELS_API_KEY}
    response = requests.post(url, headers=header)
    # location = json.loads(response.content)

    print(response.text)
    # location_dict = {
    #     "img_url" = location[""]
    # }

    return


a = "Atlanta"
s = "Georgia"

print(get_pexels(a, s))
