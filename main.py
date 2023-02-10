import database_data
import api_data


def main():
    api_data.save_data()
    conn, cursor = database_data.open_db("wufoo_db.sqlite")
    print(type(conn))
    database_data.setup_db(cursor)
    database_data.populate_db(cursor)
    database_data.close_db(cursor)


if __name__ == '__main__':
    main()
