import tkinter as tk
from tkinter import messagebox
from insert_forms.inserts_all import InsertsForm
from display_forms.raports_form import RaportsForm
from display_forms.selects_form import SelectsForm
from PIL import Image, ImageTk
from reset import reset_base

class MainForm:
    '''
    Klasa reprezentująca główną stronę aplikacji klienta.
    Z niej można przejść do dalszych części aplikacji - dodawania danych do tabel, wyświetlania tabel, oraz wyświetlania raportów
    '''
    def __init__(self, master):
        '''
        Konstruktor 
        
        Parametry:
            master (tk.Tk): Główny obiekt Tkinter, reprezentujący główne okno aplikacji.
        '''
        self.master = master
        master.title("Baza danych - Hotel")
        master.geometry("700x500")

        # Ładowanie tła z obrazka
        background_image = Image.open("images/snow.jpg") 
        background_photo = ImageTk.PhotoImage(background_image)

        # Tworzenie etykiety z tłem
        background_label = tk.Label(master, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        # Etykieta powitalna
        label = tk.Label(master, text="Baza danych - Hotel\nWybierz opcję", font=("Arial", 14))
        label.pack(pady=10, padx=20)

        # Przyciski do różnych opcji
        self.button_inserts = tk.Button(master, text="Dodawanie do tabel", command=self.open_inserts_form)
        self.button_inserts.pack(pady=10, padx=20)

        self.button_selects = tk.Button(master, text="Wyświetlanie tabel", command=self.open_selects_form)
        self.button_selects.pack(pady=10, padx=20)

        self.button_raports = tk.Button(master, text="Raporty", command=self.open_raports_form)
        self.button_raports.pack(pady=10, padx=20)

        self.button_reset = tk.Button(master, text="Reset bazy", command=reset_base)
        self.button_reset.pack(pady=10, padx=20)

    def open_inserts_form(self):
        '''Otwiera formularz do dodawania danych do tabel.'''
        inserts_form = InsertsForm(self.master)

    def open_selects_form(self):
        '''Otwiera formularz do wyświetlania tabel.'''
        selects_form = SelectsForm(self.master)

    def open_raports_form(self):
        '''Otwiera formularz do wyświetlania raportów.'''
        raports_form = RaportsForm(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    main_gui = MainForm(root)
    root.mainloop()
