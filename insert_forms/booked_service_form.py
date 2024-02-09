import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2

class BookedServiceForm:
    '''
    Formularz na dodanie danych do tabeli Booked_service
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Zarezerwuj usługę")

        self.label_service_ID = tk.Label(self.top, text="ID usługi (wymagane):")
        self.entry_service_ID = tk.Entry(self.top)

        self.label_booking_ID = tk.Label(self.top, text="ID rezerwacji na pobyt w hotelu (wymagane):")
        self.entry_booking_ID = tk.Entry(self.top)


        self.submit_button = tk.Button(self.top, text="Zarezerwuj usługę", command=self.on_submit)

        self.label_service_ID.grid(row=1, column=0, padx=30, pady=10)
        self.entry_service_ID.grid(row=1, column=1, padx=30, pady=10)

        self.label_booking_ID.grid(row=2, column=0, padx=30, pady=10)
        self.entry_booking_ID.grid(row=2, column=1, padx=30, pady=10)

        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)


    def on_submit(self):
        service_ID = self.entry_service_ID.get()
        booking_ID = self.entry_booking_ID.get()

        if not service_ID or not booking_ID:
            messagebox.showerror("Błąd", "Wszystkie wymagane pola muszą być wypełnione.\n Dopisz dane do pustych pól.")
            return
        
        if not record_exists("Hotel.Booking", "booking_ID", booking_ID):
            messagebox.showerror("Błąd", f"Brak rekordu w tabeli Booking o booking_ID równym {booking_ID}.")
            return

        if not record_exists("Hotel.Service", "service_ID", service_ID):
            messagebox.showerror("Błąd", f"Brak rekordu w tabeli Service o service_ID równym {service_ID}.")
            return

        insert_booked_service(booking_ID, service_ID)
        messagebox.showinfo("Potwierdzenie", "Zarezerwowano nową usługę!")
        print_booked_service()
        self.top.destroy()

def record_exists(table, column, value):
    try:
        conn = connect()
        cur = conn.cursor()

        query = f"SELECT 1 FROM {table} WHERE {column} = %s"
        cur.execute(query, (value,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result is not None

    except (psycopg2.Error, Exception) as error:
        print(f"Error checking record existence: {error}")
        return False

def print_booked_service():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Booked_service'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error retrieving guest data: {error}")

def insert_booked_service(booking_ID, service_ID):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Booked_service (booking_ID, service_ID) VALUES (%s, %s)'''

        c.execute(sql, (booking_ID, service_ID))
        conn.commit()
        c.close()
        conn.close()
        
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting guest: {error}")



if __name__ == "__main__":
    root = tk.Tk()
    service_form = BookedServiceForm(root)
    root.mainloop()
