import sqlite3
import api_data
import database_data


def test_get_api_data():
    test_data = api_data.get_wufoo_data()
    assert len(test_data) == 1


def test_setup_db():
    # Creates an in-memory database then connects to it
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    database_data.setup_db(cursor)

    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='wufoo_form';''')
    result = cursor.fetchone()

    assert result[0] == 'wufoo_form'

    # PRAGMA: command built in sqlite3 to retrieve data from the wufoo form
    cursor.execute('''PRAGMA table_info(wufoo_form);''')
    result = cursor.fetchall()

    assert len(result) == 14

    column_names = [rows[1] for rows in result]
    expected_columns = ['EntryID', 'First_Name', 'Last_Name', 'Title', 'Company', 'Email', 'Organization_Website',
                        'Phone_Number', 'Opportunities', 'Time_Period', 'Permission', 'Date_Created', 'Created_By',
                        'Updated_By']

    assert column_names == expected_columns
    cursor.connection.close()


