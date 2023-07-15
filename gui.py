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

# create label for personal info category
category1 = ctk.CTkLabel(root, text="Personal Information")
category1.place(x=5, y=30)

# create label for personal info
first_name = ctk.CTkLabel(root, text="First Name")
first_name.place(x=15, y=50)

# create entry buttons for personal info

root.mainloop()
