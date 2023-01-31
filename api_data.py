import requests
import sys
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth


def get_wufoo_data() -> dict:
    url = "https://devin803.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    json_response = response.json()
    return json_response


def save_data():
    with open('wufoo_data.txt', 'w') as file:
        file.write(str(get_wufoo_data()))
