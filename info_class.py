# create class for info
class ContactTracing:
    def personal_info(self, fn, sn, email, phone, address):
        first_name = (fn.get())
        surname = (sn.get())
        email_address = (email.get())
        phone_number = (phone.get())
        address = (address.get())

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
