import psycopg2
from tkinter import *
from tkinter import ttk


# Database connection setup
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="university",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)


# Fetch data from the database
def fetch_data(query):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Display data in GUI
def display_data():
    for row in tree.get_children():
        tree.delete(row)
    data = fetch_data("SELECT * FROM Teacher")
    for row in data:
        tree.insert("", "end", values=row)


# GUI Design
root = Tk()
root.title("University Database App")

# Table Display
frame = Frame(root)
frame.pack(pady=20)

columns = ("Tid", "Name", "Designation", "Salary", "DeptID")
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack()

# Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=10)

btn_display = Button(btn_frame, text="Display Data", command=display_data)
btn_display.pack(side=LEFT, padx=10)

btn_exit = Button(btn_frame, text="Exit", command=root.quit)
btn_exit.pack(side=LEFT, padx=10)

root.mainloop()
