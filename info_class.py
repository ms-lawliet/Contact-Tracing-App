# create class for info
class ContactTracing:
    def __int__(self, first_name, surname, email, phone, address):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.address = address

    def display_personal_info(self):
        first_name = (self.first_name.get())
        surname = (self.surname.get())
        email_address = (self.email.get())
        phone_number = (self.phone.get())
        home_address = (self.address.get())
        print(self.first_name, self.surname, self.email, self.phone, self.address)

    def emergency_contact(self, fn, sn, st, phone, address, rs):
        first_name = (fn.get())
        surname = (sn.get())
        phone_number = (phone.get())
        street = (st.get())
        address = (address.get())
        relationship = (rs.get())

    def contacts(self, cfn, csn, cphone, cd):
        contact_first_name = (cfn.get())
        contact_surname = (csn.get())
        contact_phone_number = (cphone.get())
        contact_date = (cd.get())
