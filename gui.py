# import modules
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from functools import partial

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


# create functions
def add_entry(fn, ln, ea, pn, ha, cfn, cln, cpn, cha, rel):
    first_name1 = fn.get()
    last_name = ln.get()
    email_address = ea.get()
    phone_number = pn.get()
    home_address = ha.get()
    contact_first_name1 = cfn.get()
    contact_last_name = cln.get()
    contact_phone_no = cpn.get()
    contact_home_address = cha.get()
    relation = rel.get()
    with open("data_entries.txt", "a") as f:
        f.write(f"\n*************************************\n")
        f.write(f"-----PERSONAL INFORMATION-----\n")
        f.write(f"Name: {last_name}, {first_name1}\n")
        f.write(f"Email Address: {email_address}\n")
        f.write(f"Phone Number: {phone_number}\n")
        f.write(f"Home Address: {home_address}\n")
        f.write("-----EMERGENCY CONTACT-----\n")
        f.write(f"Name: {contact_last_name}, {contact_first_name1}\n")
        f.write(f"Phone Number: {contact_phone_no}\n")
        f.write(f"Home Address: {contact_home_address}\n")
        f.write(f"Relationship: {relation}\n")
        f.write(f"*************************************\n")
    CTkMessagebox(title="Notice", message="Entry Added!", icon="check")


# create labels for personal info
first_name_lbl = ctk.CTkLabel(root, text="First Name")
first_name_lbl.place(x=15, y=60)
surname_lbl = ctk.CTkLabel(root, text="Surname")
surname_lbl.place(x=15, y=95)
email_lbl = ctk.CTkLabel(root, text="Email Address")
email_lbl.place(x=15, y=130)
phone_lbl = ctk.CTkLabel(root, text="Phone Number")
phone_lbl.place(x=15, y=165)
address_lbl = ctk.CTkLabel(root, text="Home Address")
address_lbl.place(x=15, y=200)

# create labels for emergency contact info
contact_first_name_lbl = ctk.CTkLabel(root, text="First Name")
contact_first_name_lbl.place(x=15, y=270)
contact_surname_lbl = ctk.CTkLabel(root, text="Surname")
contact_surname_lbl.place(x=15, y=305)
contact_phone_lbl = ctk.CTkLabel(root, text="Phone Number")
contact_phone_lbl.place(x=15, y=340)
contact_address_lbl = ctk.CTkLabel(root, text="Home Address")
contact_address_lbl.place(x=15, y=375)
relationship_lbl = ctk.CTkLabel(root, text="Relationship")
relationship_lbl.place(x=15, y=410)

# create entry buttons for personal info
first_name_entry = ctk.CTkEntry(root, textvariable=first_name)
first_name_entry.place(x=85, y=60)
surname_entry = ctk.CTkEntry(root, textvariable=surname)
surname_entry.place(x=85, y=95)
email_entry = ctk.CTkEntry(root, textvariable=email, width=175)
email_entry.place(x=105, y=130)
phone_entry = ctk.CTkEntry(root, textvariable=phone, width=175)
phone_entry.place(x=105, y=165)
address_entry = ctk.CTkEntry(root, textvariable=address, width=275)
address_entry.place(x=105, y=200)

# create entry buttons for emergency contact info
contact_first_name_entry = ctk.CTkEntry(root, textvariable=contact_first_name)
contact_first_name_entry.place(x=85, y=270)
contact_surname_entry = ctk.CTkEntry(root, textvariable=contact_surname)
contact_surname_entry.place(x=85, y=305)
contact_phone_entry = ctk.CTkEntry(root, textvariable=contact_phone, width=175)
contact_phone_entry.place(x=105, y=340)
contact_address_entry = ctk.CTkEntry(root, textvariable=contact_address, width=275)
contact_address_entry.place(x=105, y=375)
relationship_entry = ctk.CTkEntry(root, textvariable=relationship)
relationship_entry.place(x=105, y=410)

enter_data = partial(add_entry, first_name, surname, email, phone, address, contact_first_name, contact_surname,
                     contact_phone, contact_address, relationship)
add_entry_button = ctk.CTkButton(root, text="Add Entry", command=enter_data).grid(row=3, column=0)

root.mainloop()
