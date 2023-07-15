# import modules
import tkinter as tk
import customtkinter as ctk
from info_class import ContactTracing

# change theme to dark
ctk.set_appearance_mode("dark")

# create method
root = ctk.CTk()
root.geometry("475x600")
root.title("Contact Tracing App")

# create label for title
title = ctk.CTkLabel(root, text="CONTACT TRACING")
title.place(x=175, y=10)

# create category labels
category1 = ctk.CTkLabel(root, text="Personal Information")
category1.place(x=5, y=30)
category2 = ctk.CTkLabel(root, text="Emergency Contact")
category2.place(x=5, y=240)

# create labels for info
first_name = ctk.CTkLabel(root, text="First Name")
first_name.place(x=15, y=60)
surname = ctk.CTkLabel(root, text="Surname")
surname.place(x=15, y=95)
email = ctk.CTkLabel(root, text="Email Address")
email.place(x=15, y=130)
phone = ctk.CTkLabel(root, text="Phone Number")
phone.place(x=15, y=165)
address = ctk.CTkLabel(root, text="Home Address")
address.place(x=15, y=200)
first_name2 = ctk.CTkLabel(root, text="First Name")
first_name2.place(x=15, y=265)

# create entry buttons
first_name_entry = ctk.CTkEntry(root)
first_name_entry.place(x=85, y=60)
surname_entry = ctk.CTkEntry(root)
surname_entry.place(x=85, y=95)
email_entry = ctk.CTkEntry(root, width=175)
email_entry.place(x=105, y=130)
phone_entry = ctk.CTkEntry(root, width=175)
phone_entry.place(x=105, y=165)
address_entry = ctk.CTkEntry(root, width=275)
address_entry.place(x=105, y=200)
first_name2_entry = ctk.CTkEntry(root)
first_name2_entry.place(x=105, y=265)

root.mainloop()
