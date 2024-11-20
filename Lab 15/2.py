import psycopg2
from tkinter import *
from tkinter import messagebox


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
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None


def insert_record():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO Teacher (name, designation, salary, deptid) VALUES (%s, %s, %s, %s)"
            data = (name_entry.get(), designation_entry.get(), salary_entry.get(), deptid_entry.get())
            cursor.execute(query, data)
            conn.commit()
            messagebox.showinfo("Success", "Record inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert record: {e}")
        finally:
            conn.close()


def delete_record():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            tid = tid_entry.get()
            query = "DELETE FROM Teacher WHERE Tid = %s"
            cursor.execute(query, (tid,))
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Record deleted successfully!")
            else:
                messagebox.showwarning("Not Found", "No record found with the given Tid.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete record: {e}")
        finally:
            conn.close()


root = Tk()
root.title("Teacher Table Operations")

insert_frame = LabelFrame(root, text="Insert Record", padx=10, pady=10)
insert_frame.pack(padx=10, pady=10)

Label(insert_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(insert_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

Label(insert_frame, text="Designation:").grid(row=1, column=0, padx=5, pady=5)
designation_entry = Entry(insert_frame, width=30)
designation_entry.grid(row=1, column=1, padx=5, pady=5)

Label(insert_frame, text="Salary:").grid(row=2, column=0, padx=5, pady=5)
salary_entry = Entry(insert_frame, width=30)
salary_entry.grid(row=2, column=1, padx=5, pady=5)

Label(insert_frame, text="DeptID:").grid(row=3, column=0, padx=5, pady=5)
deptid_entry = Entry(insert_frame, width=30)
deptid_entry.grid(row=3, column=1, padx=5, pady=5)

insert_btn = Button(insert_frame, text="Insert Record", command=insert_record)
insert_btn.grid(row=4, column=0, columnspan=2, pady=10)

delete_frame = LabelFrame(root, text="Delete Record", padx=10, pady=10)
delete_frame.pack(padx=10, pady=10)

Label(delete_frame, text="Tid:").grid(row=0, column=0, padx=5, pady=5)
tid_entry = Entry(delete_frame, width=30)
tid_entry.grid(row=0, column=1, padx=5, pady=5)

delete_btn = Button(delete_frame, text="Delete Record", command=delete_record)
delete_btn.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
