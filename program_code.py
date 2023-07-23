from CTkMessagebox import CTkMessagebox


class Options:
    # create functions
    @staticmethod
    def add_entry(first_n, last_n, age, gender, email_add, phone_no, home_add, e_contact_fn, e_contact_ln,
                  e_contact_phone, e_contact_add, relationship, overseas, country, situation_op, a_contact_n,
                  a_contact_add, a_contact_date):
        first_name = first_n.get()
        last_name = last_n.get()
        age1 = age.get()
        gender1 = gender.get()
        email_address = email_add.get()
        phone_number = phone_no.get()
        home_address = home_add.get()
        emergency_contact_first_name = e_contact_fn.get()
        emergency_contact_last_name = e_contact_ln.get()
        emergency_contact_phone_no = e_contact_phone.get()
        emergency_contact_home_address = e_contact_add.get()
        relation = relationship.get()
        overseas_travel = overseas.get()
        travel_country = country.get()
        situation = situation_op.get()
        additional_contact_name = a_contact_n.get()
        additional_contact_address = a_contact_add.get()
        additional_contact_date = a_contact_date.get()
        name = f"{last_name}, {first_name}"
        file_name = f"Data Entries/{name}.txt"
        try:
            with open(file_name, "x") as f:
                f.write(f"-----PERSONAL INFORMATION-----\n")
                f.write(f"Name: {last_name}, {first_name}\n")
                f.write(f"Gender: {gender1}\n")
                f.write(f"Age: {age1}\n")
                f.write(f"Email Address: {email_address}\n")
                f.write(f"Phone Number: {phone_number}\n")
                f.write(f"Home Address: {home_address}\n")
                f.write("-----EMERGENCY CONTACT-----\n")
                f.write(f"Name: {emergency_contact_last_name}, {emergency_contact_first_name}\n")
                f.write(f"Phone Number: {emergency_contact_phone_no}\n")
                f.write(f"Home Address: {emergency_contact_home_address}\n")
                f.write(f"Relationship: {relation}\n")
                f.write("-----DETAILS-----\n")
                f.write(f"Has visited another country in the last two months? {overseas_travel}\n")
                f.write(f"Country visited: {travel_country}\n")
                f.write(f"Status: {situation}\n")
                f.write("---Recent Contacts---\n")
                f.write(f"Name: {additional_contact_name}\n")
                f.write(f"Address: {additional_contact_address}\n")
                f.write(f"Date of Contact: {additional_contact_date}\n")
            CTkMessagebox(title="Notice", message="Entry Added!", icon="check")
        except FileExistsError:
            CTkMessagebox(title="Notice", message="Entry Already Exists!", icon="cancel")

    @staticmethod
    def additional_contact(first_n, last_n, a_contact_n, a_contact_add, a_contact_cd):
        first_name1 = first_n.get()
        last_name = last_n.get()
        additional_contact_name = a_contact_n.get()
        additional_contact_address = a_contact_add.get()
        additional_contact_date = a_contact_cd.get()
        name = f"{last_name}, {first_name1}"
        file_name = f"Data Entries/{name}.txt"
        with open(file_name, "a") as f:
            f.write("-------------------------\n")
            f.write(f"Name: {additional_contact_name}\n")
            f.write(f"Address: {additional_contact_address}\n")
            f.write(f"Date of Contact: {additional_contact_date}\n")
        CTkMessagebox(title="Notice", message="Entry Added!", icon="check")

    @staticmethod
    def search_entry(first_n, last_n):
        search_first_name = first_n.get()
        search_last_name = last_n.get()
        name = f"{search_last_name}, {search_first_name}"
        file_name = f"Data Entries/{name}.txt"
        with open(file_name) as f:
            content = f.read()
            print(content)
