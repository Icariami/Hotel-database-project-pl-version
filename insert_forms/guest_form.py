import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2

class GuestForm:
    '''
    Formularz na dodanie danych do tabeli Guest
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Dodaj nowego gościa")

        self.label_first_name = tk.Label(self.top, text="Imię (wymagane):")
        self.entry_first_name = tk.Entry(self.top)

        self.label_last_name = tk.Label(self.top, text="Nazwisko (wymagane):")
        self.entry_last_name = tk.Entry(self.top)

        self.label_phone_number = tk.Label(self.top, text="Numer telefonu (wymagane):")
        self.entry_phone_number = tk.Entry(self.top)

        self.label_e_mail = tk.Label(self.top, text="Adres e-mail (wymagane):")
        self.entry_e_mail = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Dodaj gościa", command=self.on_submit)

        self.label_first_name.grid(row=1, column=0, padx=20, pady=10)
        self.entry_first_name.grid(row=1, column=1, padx=20, pady=10)

        self.label_last_name.grid(row=2, column=0, padx=20, pady=10)
        self.entry_last_name.grid(row=2, column=1, padx=20, pady=10)

        self.label_phone_number.grid(row=3, column=0, padx=20, pady=10)
        self.entry_phone_number.grid(row=3, column=1, padx=20, pady=10)

        self.label_e_mail.grid(row=4, column=0, padx=20, pady=10)
        self.entry_e_mail.grid(row=4, column=1, padx=20, pady=10)

        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)

    def on_submit(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        phone_number = self.entry_phone_number.get()
        e_mail = self.entry_e_mail.get()

        if not first_name or not last_name or not phone_number or not e_mail:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.\n Dopisz dane do pustych pól.")
            return

        if not first_name.isalpha():
            messagebox.showerror("Błąd", "Imię powinno składać si ę tylko z liter.\nPopraw wprowadzone dane.")
            return

        if not last_name.isalpha():
            messagebox.showerror("Błąd", "Nazwisko powinno składać się tylko z liter.\nPopraw wprowadzone dane.")
            return
        
        if not (phone_number.isdigit() and len(phone_number) in (9, 11)):
            messagebox.showerror("Błąd", "Numer telefonu powinien zawierać 9 cyfr\nlub 11 (z numerem kierunkowym).")
            return
        
        if "@" not in e_mail:
            messagebox.showerror("Błąd", "Niepoprawny adres e-mail.\nPopraw wprowadzone dane.")
            return


        insert_guest(first_name, last_name, phone_number, e_mail)
        messagebox.showinfo("Potwierdzenie", "Dodano nowego gościa!")
        print_guest()
        self.top.destroy()


def print_guest():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Guest'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error retrieving guest data: {error}")

def insert_guest(first_name, last_name, phone_number, e_mail):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Guest (first_name, last_name, phone_number, e_mail) VALUES (%s, %s, %s, %s)'''

        c.execute(sql, (first_name, last_name, phone_number, e_mail))
        conn.commit()
        c.close()
        conn.close()
        
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting guest: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    guest_form = GuestForm(root)
    root.mainloop()
