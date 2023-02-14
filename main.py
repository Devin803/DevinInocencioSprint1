import database_data
import api_data
import Gui_Window


def main():

    # api_data.save_data()
    # conn, cursor = database_data.open_db("wufoo_db.sqlite")
    # database_data.setup_db(cursor)
    # database_data.populate_db(cursor)
    app = Gui_Window.QApplication([])
    window = Gui_Window.MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()
