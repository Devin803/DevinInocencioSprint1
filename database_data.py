import json
from typing import Tuple
import sqlite3
import api_data


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo_form
                      (EntryID INTEGER PRIMARY KEY,
                      First_Name TEXT NOT NULL,
                      Last_Name TEXT NOT NULL,
                      Title TEXT NOT NULL,
                      Company TEXT NOT NULL,
                      Email TEXT NOT NULL,
                      Organization_Website TEXT NOT NULL,
                      Phone_Number INTEGER DEFAULT 0,
                      Opportunities TEXT,
                      Time_Period TEXT,
                      Permission TEXT,
                      Date_Created TEXT,
                      Created_By TEXT,
                      Updated_By TEXT);''')


def populate_db(cursor: sqlite3.Cursor):
    form_data = api_data.get_wufoo_data()
    for item in form_data['Entries']:
        cursor.execute(f'''INSERT INTO wufoo_form VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (item['EntryId'],
                        item.get('Field17', ''),
                        item.get('Field18', ''),
                        item.get('Field4', ''),
                        item.get('Field7', ''),
                        item.get('Field20', ''),
                        item.get('Field8', ''),
                        item.get('Field9', ''),
                        item.get('Field23', ''),
                        item.get('Field121', ''),
                        item.get('Field224', ''),
                        item.get('DateCreated', ''),
                        item.get('CreatedBy', ''),
                        item.get('UpdatedBy', '')))
    cursor.connection.commit()
