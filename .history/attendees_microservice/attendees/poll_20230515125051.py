import json
import requests
from .models import ConferenceVO

def get_conferences():
    url = "http://monolith:8000/api/conferences"
    response = requests.get(url)
    