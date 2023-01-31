import sys
import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth
import sqlite3
from typing import Tuple


def get_wufoo_data() -> dict:
    url = "https://devin803.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    json_response = response.json()
    return json_response


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def save_data():
    with open('wufoo_data.txt', 'w') as file:
        file.write(str(get_wufoo_data()))


def main():
    save_data()
    open_db("wufoo_db.sqlite")


if __name__ == '__main__':
    main()
