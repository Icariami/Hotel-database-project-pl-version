import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2


class HotelForm:
    '''
    Formularz na dodanie danych do tabeli Hotel
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Dodaj nowy hotel")

        self.label_name = tk.Label(self.top, text="Nazwa (wymagane):")
        self.entry_name = tk.Entry(self.top)

        self.label_address = tk.Label(self.top, text="Adres (wymagane):")
        self.entry_address = tk.Entry(self.top)

        self.label_phone_number = tk.Label(self.top, text="Numer telefonu (wymagane):")
        self.entry_phone_number = tk.Entry(self.top)

        self.label_e_mail = tk.Label(self.top, text="Adres e-mail (wymagane):")
        self.entry_e_mail = tk.Entry(self.top)

        self.label_description = tk.Label(self.top, text="Opis:")
        self.entry_description = tk.Entry(self.top)

        self.label_star_rating = tk.Label(self.top, text="Gwiazdki (wymagane):")
        self.entry_star_rating = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Dodaj hotel", command=self.on_submit)

        self.label_name.grid(row=1, column=0, padx=20, pady=10)
        self.entry_name.grid(row=1, column=1, padx=20, pady=10)

        self.label_address.grid(row=2, column=0, padx=20, pady=10)
        self.entry_address.grid(row=2, column=1, padx=20, pady=10)

        self.label_phone_number.grid(row=3, column=0, padx=20, pady=10)
        self.entry_phone_number.grid(row=3, column=1, padx=20, pady=10)

        self.label_e_mail.grid(row=4, column=0, padx=20, pady=10)
        self.entry_e_mail.grid(row=4, column=1, padx=20, pady=10)

        self.label_description.grid(row=5, column=0, padx=20, pady=10)
        self.entry_description.grid(row=5, column=1, padx=20, pady=10)

        self.label_star_rating.grid(row=6, column=0, padx=20, pady=10)
        self.entry_star_rating.grid(row=6, column=1, padx=20, pady=10)

        self.submit_button.grid(row=7, column=0, columnspan=2, pady=20)

    def on_submit(self):
        name = self.entry_name.get()
        address = self.entry_address.get()
        phone_number = self.entry_phone_number.get()
        e_mail = self.entry_e_mail.get()
        description = self.entry_description.get()
        star_rating = self.entry_star_rating.get()

        if not name or not address or not phone_number or not e_mail:
            messagebox.showerror("Błąd", "Wszystkie wymagane pola muszą być wypełnione.\n Dopisz dane do pustych pól.")
            return

        if not (phone_number.isdigit() and len(phone_number) in (9, 11)):
            messagebox.showerror("Błąd", "Numer telefonu powinien zawierać 9 cyfr\nlub 11 (z numerem kierunkowym).")
            return
        
        if "@" not in e_mail:
            messagebox.showerror("Błąd", "Niepoprawny adres e-mail.\nPopraw wprowadzone dane.")
            return

        insert_hotel(name, address, phone_number, e_mail, description, star_rating)
        messagebox.showinfo("Potwierdzenie", "Dodano nowy hotel!")
        print_hotel()
        self.top.destroy()

def insert_hotel(name, address, phone_number, e_mail, description, star_rating):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Hotel (name, address, phone_number, e_mail, description, star_rating) VALUES (%s, %s, %s, %s, %s, %s)'''

        c.execute(sql, (name, address, phone_number, e_mail, description, star_rating))
        conn.commit()
        c.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting data: {error}")


def print_hotel():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Hotel'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting data: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    hotel_form = HotelForm(root)
    root.mainloop()