import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2
from datetime import datetime

class BookingForm:
    '''
    Formularz na dodanie danych do tabeli Booking
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Dodaj nową rezerwację")

        self.label_room_id = tk.Label(self.top, text="ID pokoju (wymagane):")
        self.entry_room_id = tk.Entry(self.top)

        self.label_guest_id = tk.Label(self.top, text="ID gościa (wymagane):")
        self.entry_guest_id = tk.Entry(self.top)

        self.label_check_in_date = tk.Label(self.top, text="Data zameldowania (wymagane, format: RRRR-MM-DD):")
        self.entry_check_in_date = tk.Entry(self.top)

        self.label_check_out_date = tk.Label(self.top, text="Data wymeldowania (wymagane, format: RRRR-MM-DD):")
        self.entry_check_out_date = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Dodaj rezerwację", command=self.on_submit)

        self.label_room_id.grid(row=1, column=0, padx=20, pady=10)
        self.entry_room_id.grid(row=1, column=1, padx=20, pady=10)

        self.label_guest_id.grid(row=2, column=0, padx=20, pady=10)
        self.entry_guest_id.grid(row=2, column=1, padx=20, pady=10)

        self.label_check_in_date.grid(row=3, column=0, padx=20, pady=10)
        self.entry_check_in_date.grid(row=3, column=1, padx=20, pady=10)

        self.label_check_out_date.grid(row=4, column=0, padx=20, pady=10)
        self.entry_check_out_date.grid(row=4, column=1, padx=20, pady=10)

        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    def on_submit(self):
        room_id = self.entry_room_id.get()
        guest_id = self.entry_guest_id.get()
        check_in_date = self.entry_check_in_date.get()
        check_out_date = self.entry_check_out_date.get()

        if not room_id or not guest_id or not check_in_date or not check_out_date:
            messagebox.showerror("Błąd", "Wszystkie wymagane pola muszą być wypełnione.\n Dopisz dane do pustych pól.")
            return
        
        if not record_exists("Hotel.Room", "room_ID", room_id):
            messagebox.showerror("Błąd", f"Brak rekordu w tabeli Room o room_ID równym {room_id}.")
            return

        if not record_exists("Hotel.Guest", "guest_ID", guest_id):
            messagebox.showerror("Błąd", f"Brak rekordu w tabeli Guest o guest_ID równym {guest_id}.")
            return

        try:
            check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Błąd", "Nieprawidłowy format daty. Poprawny format to RRRR-MM-DD.")
            return

        if check_out_date <= check_in_date:
            messagebox.showerror("Błąd", "Data wymeldowania musi być późniejsza niż data zameldowania.")
            return
    

        try:
            insert_booking(room_id, guest_id, check_in_date, check_out_date)
            messagebox.showinfo("Potwierdzenie", "Dodano nową rezerwację!")
            print_booking()
            self.top.destroy()
        except Exception as e:
            messagebox.showerror("Błąd", "Pokój jest już zajęty w podanym terminie.")

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

def print_booking():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Booking'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error retrieving guest data: {error}")

def insert_booking(room_id, guest_id, check_in_date, check_out_date):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Booking (room_id, guest_id, check_in_date, check_out_date) VALUES (%s, %s, %s, %s)'''

        c.execute(sql, (room_id, guest_id, check_in_date, check_out_date))
        conn.commit()
        c.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        raise Exception(f"Error inserting booking: {error}")


if __name__ == "__main__":
    root = tk.Tk()
    booking_form = BookingForm(root)
    root.mainloop()
