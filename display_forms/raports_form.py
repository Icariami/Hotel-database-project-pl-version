import tkinter as tk
from tkinter import messagebox, ttk
from DB_connect import connect
import psycopg2
from PIL import Image, ImageTk

class RaportsForm:
    '''
    Formularz zawierający przyciski otwerające raporty bazujące na widokach wykonanych na różnych elementach w bazie dancyh
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Raporty")

        background_image = Image.open("images/snowysky.jpg!d") 
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(self.top, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label_first_raport = tk.Label(self.top, text="Raport pierwszy - Zestawienie przychodów dla hotelu Chata w roku 2023:")
        self.button_first_raport = tk.Button(self.top, text="Zobacz raport 1", command=self.first_raport)

        self.label_second_raport = tk.Label(self.top, text="Raport drugi - Zestawienie gości, którzy skorzystali z którejś z usług \noferowanych przez hotel oraz wystawili o niej opinię:")
        self.button_second_raport = tk.Button(self.top, text="Zobacz raport 2", command=self.second_raport)

        self.label_third_raport = tk.Label(self.top, text="Raport trzeci - Zestawienie gości, którzy ponownie skorzystali z hotelu, \nwraz z średnią długością ich odwiedzin:")
        self.button_third_raport = tk.Button(self.top, text="Zobacz raport 3", command=self.third_raport)

        self.label_first_raport.grid(row=1, column=0, padx=10, pady=10)
        self.button_first_raport.grid(row=1, column=1, padx=10, pady=10)

        self.label_second_raport.grid(row=2, column=0, padx=10, pady=10)
        self.button_second_raport.grid(row=2, column=1, padx=10, pady=10)

        self.label_third_raport.grid(row=3, column=0, padx=10, pady=10)
        self.button_third_raport.grid(row=3, column=1, padx=10, pady=10)

    def first_raport(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Monthly_revenue''')
        self.show_first_raport(result, column_names)

    def second_raport(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Guest_Service_Reservations_With_Reviews''')
        self.show_second_raport(result, column_names)

    def third_raport(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Average_duration_of_stay''')
        self.show_third_raport(result, column_names)

    def execute_sql_query(self, query):
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute(query)
            column_names = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()
            connection.close()
            return result, column_names
        except psycopg2.Error as e:
            messagebox.showerror("Błąd", f"Błąd podczas wykonania zapytania SQL: {str(e)}")
            
    def show_second_raport(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Raport 2 - Zestawienie gości, którzy skorzystali z którejś z usług oferowanych przez hotel oraz wystawili o niej opinię")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER, width=200)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=100)
        result_treeview.column("#2", width=100)
        result_treeview.column("opinia", width=500)
        result_treeview.column("ocena", width=50)
        result_window.geometry("1150x500")  
        result_treeview.pack(expand=True, fill="both")

    def show_first_raport(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Raport 1 - Zestawienie przychodów dla hotelu Chata w roku 2023")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER, width=200)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=60)
        result_window.geometry("700x400") 
        result_treeview.pack(expand=True, fill="both")

    def show_third_raport(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Raport 3 - Zestawienie gości, którzy ponownie skorzystali z hotelu, wraz z średnią długością ich odwiedzin")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER, width=200)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=100)
        result_treeview.column("#2", width=100)
        result_treeview.column("#3", width=150)
        result_window.geometry("700x400") 
        result_treeview.pack(expand=True, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    reports_gui = RaportsForm(root)
    root.mainloop()
