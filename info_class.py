# create class for info
class ContactTracing:
    @staticmethod
    # create functions
    def add_entry(fn, ln, ea, pn, ha):
        first_name1 = fn.get()
        last_name = ln.get()
        email_address = ea.get()
        phone_number = pn.get()
        home_address = ha.get()
        with open("data_entries.txt", "a") as f:
            f.write(f"Name: {last_name}, {first_name1}\n")
            f.write(f"Email Address: {email_address}\n")
            f.write(f"Phone Number: {phone_number}\n")
            f.write(f"Home Address: {home_address}\n")
            f.write("\n")
