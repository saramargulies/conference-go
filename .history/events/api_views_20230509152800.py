from django.http import JsonResponse

from .models import Conference, Location
from common.json import ModelEncoder


class ConferenceDetailEncoder(ModelEncoder):
    model = Conference
    properties = [
        "name",
        "description",
        # "starts",
        # "ends",
        # "created",
        # "updated",

    ]


def api_list_conferences(request):

    response = []
    conferences = Conference.objects.all()
    for conference in conferences:
        response.append(
            {
                "name": conference.name,
                "href": conference.get_api_url(),
            }
        )
    return JsonResponse({"conferences": response})


def api_show_conference(request, id):

    conference = Conference.objects.get(id=id)
    # return JsonResponse(
    #     {
    #         "name": conference.name,
    #         "starts": conference.starts,
    #         "ends": conference.ends,
    #         "description": conference.description,
    #         "created": conference.created,
    #         "updated": conference.updated,
    #         "max_presentations": conference.max_presentations,
    #         "max_attendees": conference.max_attendees,
    #         "location": {
    #             "name": conference.location.name,
    #             "href": conference.location.get_api_url(),
    #         },
    #     }
    # )

    return JsonResponse(
        conference, encoder=ConferenceDetailEncoder, safe=False
    )


def api_list_locations(request):

    response = []
    locations = Location.objects.all()
    for location in locations:
        response.append(
            {
                "name": location.name,
                "href": location.get_api_url(),
            }
        )
    return JsonResponse({"locations": response})


def api_show_location(request, id):
    """
    Returns the details for the Location model specified
    by the id parameter.

    This should return a dictionary with the name, city,
    room count, created, updated, and state abbreviation.

    {
        "name": location's name,
        "city": location's city,
        "room_count": the number of rooms available,
        "created": the date/time when the record was created,
        "updated": the date/time when the record was updated,
        "state": the two-letter abbreviation for the state,
    }
    """

    location = Location.objects.get(id=id)
    return JsonResponse(
        {
            "name": location.name,
            "city": location.city,
            "room_count": location.room_count,
            "created": location.created,
            "updated": location.updated,
            "state": location.state.abbreviation,
        }
    )
