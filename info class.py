# create class for info
class ContactTracing:
    def personal_info(self, fn, sn, email, phone, st, cprov, zipc):
        first_name = (fn.get())
        surname = (sn.get())
        email_address = (email.get())
        phone_number = (phone.get())
        street = (st.get())
        city_or_province = (cprov.get())
        zip_code = (zipc.get())

    def emergency_contact(self, fn, sn, st, phone, cprov, zipc, rs):
        first_name = (fn.get())
        surname = (sn.get())
        phone_number = (phone.get())
        street = (st.get())
        city_or_province = (cprov.get())
        zip_code = (zipc.get())
        relationship = (rs.get())

    def contacts(self, cfn, csn, cphone, cd):
        contact_first_name = (cfn.get())
        contact_surname = (csn.get())
        contact_phone_number = (cphone.get())
        contact_date = (cd.get())
