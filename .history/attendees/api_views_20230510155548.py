from django.http import JsonResponse
from common.json import ModelEncoder
from events.models import Conference
from django.views.decorators.http import require_http_methods
import json


from .models import Attendee


class ConferenceVODEncoder(ModelEncoder):
    model = Conference
    properties = ["name"]


class AttendeeDetailEncoder(ModelEncoder):
    model = Attendee
    properties = ["name", "email", "company_name", "created", "conference"]
    encoders = {"conference": ConferenceVODEncoder()}


class AttendeeListEncoder(ModelEncoder):
    model = Attendee
    properties = ["name"]


@require_http_methods(["GET", "POST"])
def api_list_attendees(request, conference_id):
    """
    Lists the attendees names and the link to the attendee
    for the specified conference id.

    Returns a dictionary with a single key "attendees" which
    is a list of attendee names and URLS. Each entry in the list
    is a dictionary that contains the name of the attendee and
    the link to the attendee's information.

    {
        "attendees": [
            {
                "name": attendee's name,
                "href": URL to the attendee,
            },
            ...
        ]
    }
    """
    if request.method == "GET":
        attendees = Attendee.objects.filter(conference=conference_id)
        return JsonResponse(
            {"attendees": attendees},
            encoder=AttendeeListEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            conference = Conference.objects.get(id=conference_id)
            content["conference"] = conference
        except Conference.DoesNotExist:
            return JsonResponse({"message": "Invalid conference"}, status=400)
        attendee = Attendee.objects.create(**content)
        return JsonResponse(
            attendee, encoder=AttendeeDetailEncoder, safe=False
        )


def api_show_attendee(request, id):
    """
    Returns the details for the Attendee model specified
    by the id parameter.

    This should return a dictionary with email, name,
    company name, created, and conference properties for
    the specified Attendee instance.

    {
        "email": the attendee's email,
        "name": the attendee's name,
        "company_name": the attendee's company's name,
        "created": the date/time when the record was created,
        "conference": {
            "name": the name of the conference,
            "href": the URL to the conference,
        }
    }
    """
    attendee = Attendee.objects.get(id=id)
    return JsonResponse(
        {
            "email": attendee.email,
            "name": attendee.name,
            "company_name": attendee.company_name,
            "created": attendee.created,
            "conference": {
                "name": attendee.conference.name,
                "href": attendee.conference.get_api_url(),
            },
        }
    )

@require_http_methods(["PUT", "GET"])
def api_show_conference(request, id):
    """
    Returns the details for the Conference model specified
    by the id parameter.

    This should return a dictionary with the name, starts,
    ends, description, created, updated, max_presentations,
    max_attendees, and a dictionary for the location containing
    its name and href.

    {
        "name": the conference's name,
        "starts": the date/time when the conference starts,
        "ends": the date/time when the conference ends,
        "description": the description of the conference,
        "created": the date/time when the record was created,
        "updated": the date/time when the record was updated,
        "max_presentations": the maximum number of presentations,
        "max_attendees": the maximum number of attendees,
        "location": {
            "name": the name of the location,
            "href": the URL for the location,
        }
    }
    """
    if request.method == "GET":
        conference = Conference.objects.get(id=id)
        return JsonResponse(
            conference, encoder=ConferenceDetailEncoder, safe=False
        )
    elif request.method == "PUT":
        content = json.loads(request.body)
        try:
            location = Location.objects.get(id=content["location"])
            content["location"] = location
        except Location.DoesNotExist:
            return JsonResponse({"message": "Invalid location id"}, status=400)
        conference = Conference.objects.filter(id=id).update(**content)
        conference = Conference.objects.get(id=id)
        return JsonResponse(
            conference, encoder=ConferenceDetailEncoder, safe=False
        )



# return JSONResponse(
#     attendee,
#     encoder=ModelEncoder
# )
