import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2

class ServiceForm:
    '''
    Formularz na dodanie danych do tabeli Service
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Dodaj nową usługę")

        self.label_service_name = tk.Label(self.top, text="Nazwa usługi (wymagane):")
        self.entry_service_name = tk.Entry(self.top)

        self.label_price = tk.Label(self.top, text="Cena (wymagane):")
        self.entry_price = tk.Entry(self.top)

        self.label_description = tk.Label(self.top, text="Opis:")
        self.entry_description = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Dodaj usługę", command=self.on_submit)

        self.label_service_name.grid(row=1, column=0, padx=20, pady=10)
        self.entry_service_name.grid(row=1, column=1, padx=20, pady=10)

        self.label_price.grid(row=2, column=0, padx=20, pady=10)
        self.entry_price.grid(row=2, column=1, padx=20, pady=10)

        self.label_description.grid(row=3, column=0, padx=20, pady=10)
        self.entry_description.grid(row=3, column=1, padx=20, pady=10)

        self.submit_button.grid(row=4, column=0, columnspan=2, pady=20)


    def on_submit(self):
        service_name = self.entry_service_name.get()
        price = self.entry_price.get()
        description = self.entry_description.get()

        if not service_name or not price:
            messagebox.showerror("Błąd", "Wszystkie wymagane pola muszą być wypełnione.\n Dopisz dane do pustych pól.")
            return
        
        if not (price.isdigit()):
            messagebox.showerror("Błąd", "Nieprawidłowa cena.")
            return

        insert_service(service_name, description, price)
        messagebox.showinfo("Potwierdzenie", "Dodano nową usługę!")
        print_service()
        self.top.destroy()


def print_service():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Service'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error retrieving guest data: {error}")

def insert_service(name, description, price):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Service (name, description, price) VALUES (%s, %s, %s)'''

        c.execute(sql, (name, description, price))
        conn.commit()
        c.close()
        conn.close()
        
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting guest: {error}")



if __name__ == "__main__":
    root = tk.Tk()
    service_form = ServiceForm(root)
    root.mainloop()
