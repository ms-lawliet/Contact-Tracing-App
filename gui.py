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
label_title = ctk.CTkLabel(root, text="CONTACT TRACING")
label_title.place(x=175, y=10)

# create variables
# create label for personal info
# create entry buttons for personal info

root.mainloop()
