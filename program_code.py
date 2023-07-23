from CTkMessagebox import CTkMessagebox


class Options:
    # create functions
    @staticmethod
    def add_entry(fn, ln, age, gdr, ea, pn, ha, cfn, cln, cpn, cha, rel, oot, cty):
        first_name1 = fn.get()
        last_name = ln.get()
        age1 = age.get()
        gender = gdr.get()
        email_address = ea.get()
        phone_number = pn.get()
        home_address = ha.get()
        contact_first_name1 = cfn.get()
        contact_last_name = cln.get()
        contact_phone_no = cpn.get()
        contact_home_address = cha.get()
        relation = rel.get()
        overseas_travel = oot.get()
        country = cty.get()
        name = f"{last_name}, {first_name1}"
        file_name = f"Data Entries/{name}.txt"
        try:
            with open(file_name, "x") as f:
                f.write(f"*************************************\n")
                f.write(f"-----PERSONAL INFORMATION-----\n")
                f.write(f"Name: {last_name}, {first_name1}\n")
                f.write(f"Gender: {gender}\n")
                f.write(f"Age: {age1}\n")
                f.write(f"Email Address: {email_address}\n")
                f.write(f"Phone Number: {phone_number}\n")
                f.write(f"Home Address: {home_address}\n")
                f.write("-----EMERGENCY CONTACT-----\n")
                f.write(f"Name: {contact_last_name}, {contact_first_name1}\n")
                f.write(f"Phone Number: {contact_phone_no}\n")
                f.write(f"Home Address: {contact_home_address}\n")
                f.write(f"Relationship: {relation}\n")
                f.write("-----DETAILS-----\n")
                f.write(f"Has visited another country in the last two months? {overseas_travel}\n")
                f.write(f"Country visited: {country}\n")
                f.write(f"*************************************\n")
            CTkMessagebox(title="Notice", message="Entry Added!", icon="check")
        except FileExistsError:
            CTkMessagebox(title="Notice", message="Entry Already Exists!", icon="cancel")

    @staticmethod
    def search_entry(fn, ln):
        search_first_name = fn.get()
        search_last_name = ln.get()
        name = f"{search_last_name}, {search_first_name}"
        file_name = f"Data Entries/{name}.txt"
        with open(file_name) as f:
            content = f.read()
            print(content)
