# import modules
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from functools import partial
from program_code import Options

# change theme to dark
ctk.set_appearance_mode("dark")

# create method
root = ctk.CTk()
root.geometry("300x300")
root.title("Contact Tracing App")


class OptionsWindow:
    @staticmethod
    def open_entry_window():
        # new window
        window = ctk.CTkToplevel(root)
        window.geometry("475x600")
        window.title("Add Entry")
        root.withdraw()

        # create label for title
        title = ctk.CTkLabel(window, text="CONTACT TRACING", font=("Fixedsys", 30), text_color="dodger blue")
        title.place(x=120, y=5)

        # create category labels
        category1 = ctk.CTkLabel(window, text="Personal Information", font=("Fixedsys", 15))
        category1.place(x=5, y=30)
        category2 = ctk.CTkLabel(window, text="Emergency Contact", font=("Fixedsys", 15))
        category2.place(x=5, y=240)

        # create variables
        first_name = ctk.StringVar()
        surname = ctk.StringVar()
        email = ctk.StringVar()
        phone = ctk.StringVar()
        address = ctk.StringVar()
        contact_first_name = ctk.StringVar()
        contact_surname = ctk.StringVar()
        contact_phone = ctk.StringVar()
        contact_address = ctk.StringVar()
        relationship = ctk.StringVar()

        # create labels for personal info
        personal_info_frame = ctk.CTkFrame(window, width=450, height=180, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        personal_info_frame.place(x=10, y=55)
        first_name_lbl = ctk.CTkLabel(window, text="First Name", font=("Fixedsys", 12), text_color="dodger blue")
        first_name_lbl.place(x=15, y=60)
        surname_lbl = ctk.CTkLabel(window, text="Surname", font=("Fixedsys", 12), text_color="dodger blue")
        surname_lbl.place(x=15, y=95)
        email_lbl = ctk.CTkLabel(window, text="Email Address", font=("Fixedsys", 12), text_color="dodger blue")
        email_lbl.place(x=15, y=130)
        phone_lbl = ctk.CTkLabel(window, text="Phone Number", font=("Fixedsys", 12), text_color="dodger blue")
        phone_lbl.place(x=15, y=165)
        address_lbl = ctk.CTkLabel(window, text="Home Address", font=("Fixedsys", 12), text_color="dodger blue")
        address_lbl.place(x=15, y=200)

        # create labels for emergency contact info
        personal_info_frame = ctk.CTkFrame(window, width=450, height=180, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        personal_info_frame.place(x=10, y=265)
        contact_first_name_lbl = ctk.CTkLabel(window, text="First Name", font=("Fixedsys", 12), text_color="dodger blue")
        contact_first_name_lbl.place(x=15, y=270)
        contact_surname_lbl = ctk.CTkLabel(window, text="Surname", font=("Fixedsys", 12), text_color="dodger blue")
        contact_surname_lbl.place(x=15, y=305)
        contact_phone_lbl = ctk.CTkLabel(window, text="Phone Number", font=("Fixedsys", 12), text_color="dodger blue")
        contact_phone_lbl.place(x=15, y=340)
        contact_address_lbl = ctk.CTkLabel(window, text="Home Address", font=("Fixedsys", 12), text_color="dodger blue")
        contact_address_lbl.place(x=15, y=375)
        relationship_lbl = ctk.CTkLabel(window, text="Relationship", font=("Fixedsys", 12), text_color="dodger blue")
        relationship_lbl.place(x=15, y=410)

        # create entry buttons for personal info
        first_name_entry = ctk.CTkEntry(window, textvariable=first_name)
        first_name_entry.place(x=100, y=60)
        surname_entry = ctk.CTkEntry(window, textvariable=surname)
        surname_entry.place(x=85, y=95)
        email_entry = ctk.CTkEntry(window, textvariable=email, width=175)
        email_entry.place(x=125, y=130)
        phone_entry = ctk.CTkEntry(window, textvariable=phone, width=175)
        phone_entry.place(x=120, y=165)
        address_entry = ctk.CTkEntry(window, textvariable=address, width=275)
        address_entry.place(x=120, y=200)

        # create entry buttons for emergency contact info
        contact_first_name_entry = ctk.CTkEntry(window, textvariable=contact_first_name)
        contact_first_name_entry.place(x=100, y=270)
        contact_surname_entry = ctk.CTkEntry(window, textvariable=contact_surname)
        contact_surname_entry.place(x=85, y=305)
        contact_phone_entry = ctk.CTkEntry(window, textvariable=contact_phone, width=175)
        contact_phone_entry.place(x=120, y=340)
        contact_address_entry = ctk.CTkEntry(window, textvariable=contact_address, width=275)
        contact_address_entry.place(x=120, y=375)
        relationship_entry = ctk.CTkEntry(window, textvariable=relationship)
        relationship_entry.place(x=120, y=410)

        enter_data = partial(Options.add_entry, first_name, surname, email, phone, address, contact_first_name,
                             contact_surname, contact_phone, contact_address, relationship)
        add_entry_button = ctk.CTkButton(window, text="Add Entry", command=enter_data)
        add_entry_button.place(x=95, y=500)

    @staticmethod
    def search_entry_window():
        root.withdraw()
        window2 = ctk.CTkToplevel(root)
        window2.geometry("300x300")
        window2.title("Search Entry")

        first_name = ctk.StringVar()
        surname = ctk.StringVar()

        first_name_lbl = ctk.CTkLabel(window2, text="First Name")
        first_name_lbl.place(x=15, y=60)
        surname_lbl = ctk.CTkLabel(window2, text="Surname")
        surname_lbl.place(x=15, y=95)

        first_name_entry = ctk.CTkEntry(window2, textvariable=first_name)
        first_name_entry.place(x=85, y=60)
        surname_entry = ctk.CTkEntry(window2, textvariable=surname)
        surname_entry.place(x=85, y=95)

        search_data = partial(Options.search_entry, first_name, surname)
        search_entry_button = ctk.CTkButton(window2, text="Search Entry", command=search_data)
        search_entry_button.place(x=85, y=150)


title_lbl = ctk.CTkLabel(root, text="CONTACT\nTRACING", font=("Fixedsys", 35), text_color="dodger blue")
title_lbl.place(x=70, y=60)

add_button = ctk.CTkButton(root, text="ADD ENTRY", font=("Fixedsys", 10), command=OptionsWindow.open_entry_window)
add_button.place(x=85, y=160)
search_button = ctk.CTkButton(root, text="SEARCH ENTRY", font=("Fixedsys", 10), command=OptionsWindow.search_entry_window)
search_button.place(x=85, y=195)

root.mainloop()
