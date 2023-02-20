import tkinter as tk
import sqlite3


def create_window():
    # Create the main window
    root = tk.Tk()
    root.title("Wufoo Form Data")

    # Create a table to display the data
    table = tk.Frame(root)
    table.pack(padx=10, pady=10)

    # Create the header row
    header = tk.Frame(table)
    header.pack(fill="x")
    tk.Label(header, text="Entry ID", width=10).pack(side="left")
    tk.Label(header, text="First Name", width=20).pack(side="left")
    tk.Label(header, text="Last Name", width=20).pack(side="left")
    tk.Label(header, text="Title", width=20).pack(side="left")
    tk.Label(header, text="Company", width=20).pack(side="left")
    tk.Label(header, text="Email", width=30).pack(side="left")
    tk.Label(header, text="Website", width=30).pack(side="left")
    tk.Label(header, text="Phone", width=15).pack(side="left")
    tk.Label(header, text="Opportunities", width=30).pack(side="left")
    tk.Label(header, text="Time Period", width=30).pack(side="left")
    tk.Label(header, text="Permission", width=10).pack(side="left")

    # Create a connection to the database
    conn = sqlite3.connect("wufoo_db.sqlite")
    cursor = conn.cursor()

    # Retrieve the data from the wufoo_form table
    cursor.execute("SELECT * FROM wufoo_form")
    data = cursor.fetchall()

    # Create a row for each entry in the table
    for row in data:
        entry = tk.Frame(table)
        entry.pack(fill="x")
        tk.Label(entry, text=row[0], width=10).pack(side="left")
        tk.Label(entry, text=row[1], width=20).pack(side="left")
        tk.Label(entry, text=row[2], width=20).pack(side="left")
        tk.Label(entry, text=row[3], width=20).pack(side="left")
        tk.Label(entry, text=row[4], width=20).pack(side="left")
        tk.Label(entry, text=row[5], width=30).pack(side="left")
        tk.Label(entry, text=row[6], width=30).pack(side="left")
        tk.Label(entry, text=row[7], width=15).pack(side="left")
        tk.Label(entry, text=row[8], width=30).pack(side="left")
        tk.Label(entry, text=row[9], width=30).pack(side="left")
        tk.Label(entry, text=row[10], width=10).pack(side="left")

    # Close the database connection
    conn.close()

    # Start the main event loop
    root.mainloop()
