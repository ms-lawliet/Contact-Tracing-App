from CTkMessagebox import CTkMessagebox


class Options:
    # create functions
    @staticmethod
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

    @staticmethod
    def search_entry(fn, ln):
        with open("data_entries.txt") as f:
            search_first_name = fn.get()
            search_last_name = ln.get()
            name = f"{search_last_name}, {search_first_name}"
            entries = f.read()
            if name in entries:
                print(name)
            else:
                print("No data found.")
