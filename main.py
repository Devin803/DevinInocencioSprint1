import database_data
import api_data


def main():
    api_data.save_data()
    database_data.open_db("wufoo_db.sqlite")


if __name__ == '__main__':
    main()
