import tkinter as tk
from tkinter import messagebox
from insert_forms.guest_form import GuestForm
from insert_forms.hotel_form import HotelForm
from insert_forms.room_type_form import RoomTypeForm
from insert_forms.room_form import RoomForm
from insert_forms.booking_form import BookingForm
from insert_forms.service_form import ServiceForm
from insert_forms.booked_service_form import BookedServiceForm
from insert_forms.review_form import ReviewForm
from PIL import Image, ImageTk


class InsertsForm:
    '''
    Formularz zawierający przyciski przekierowujące do formularzy dla poszczególnych tabel.
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Dodawanie do tabel")
        self.top.geometry("300x380")

        background_image = Image.open("images/tree3.jpeg") 
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(self.top, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button_add_guest = tk.Button(self.top, text="Dodaj gościa do tabeli 'Guest'", command=self.open_guest_form)
        self.button_add_guest.pack(pady=10)

        self.button_add_hotel = tk.Button(self.top, text="Dodaj hotel do tabeli 'Hotel'", command=self.open_hotel_form)
        self.button_add_hotel.pack(pady=10)

        self.button_add_room_type = tk.Button(self.top, text="Dodaj rodzaj pokoju do tabeli 'Room_type'", command=self.open_room_type_form)
        self.button_add_room_type.pack(pady=10)

        self.button_add_room = tk.Button(self.top, text="Dodaj pokój do tabeli 'Room'", command=self.open_room_form)
        self.button_add_room.pack(pady=10)

        self.button_add_booking = tk.Button(self.top, text="Dodaj rezerwację do tabeli 'Booking'", command=self.open_booking_form)
        self.button_add_booking.pack(pady=10)

        self.button_add_service = tk.Button(self.top, text="Dodaj usługę do tabeli 'Service'", command=self.open_service_form)
        self.button_add_service.pack(pady=10)

        self.button_add_booked_service = tk.Button(self.top, text="Zarezerwuj usługę w tabeli 'Booked_service'", command=self.open_booked_service_form)
        self.button_add_booked_service.pack(pady=10)

        self.button_add_review = tk.Button(self.top, text="Dodaj recenzję do tabeli 'Review'", command=self.open_review_form)
        self.button_add_review.pack(pady=10)

    def open_guest_form(self):
        guest_form = GuestForm(self.master)

    def open_hotel_form(self):
        hotel_form = HotelForm(self.master)

    def open_room_type_form(self):
        room_type_form = RoomTypeForm(self.master)

    def open_room_form(self):
        room_form = RoomForm(self.master)

    def open_booking_form(self):
        booking_form = BookingForm(self.master)

    def open_service_form(self):
        service_form = ServiceForm(self.master)

    def open_booked_service_form(self):
        booked_service_form = BookedServiceForm(self.master)

    def open_review_form(self):
        review_form = ReviewForm(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    main_gui = InsertsForm(root)
    root.mainloop()
