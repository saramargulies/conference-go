import json, requests


def get_pexels(city, state):
    query = {"city": city, "state": state}
    url = "https://api.pexels.com/v1/search"
    header = {
        "Authorization": "DEAQdjngSD8jcPzadz21tww7qTjNiUh17ETpxV0ZcMEWhH9ugdfyxqlw"
    }
    response = requests.post(url, params=query, headers=header)
    location = json.loads(response.content)
    return location


# def get_weather_data(city, state):
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
