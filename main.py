import sys
import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth


def get_wufoo_data() -> dict:
    url = "https://devin803.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    json_response = response.json()
    return json_response  # json response will be either a dictionary or a list of dictionaries
    # each dictionary represents a json object
