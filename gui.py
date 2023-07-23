# import modules
import customtkinter as ctk
from functools import partial
from program_code import Options

# change theme to dark
ctk.set_appearance_mode("dark")

# create method
root = ctk.CTk()
root.geometry("300x300")
root.title("Contact Tracing App")


class OptionsWindow:
    @staticmethod
    def open_entry_window():
        # new window
        window = ctk.CTkToplevel(root)
        window.geometry("875x600")
        window.title("Add Entry")
        root.withdraw()

        # create label for title
        title = ctk.CTkLabel(window, text="CONTACT TRACING", font=("FixedSys", 30), text_color="dodger blue")
        title.place(x=300, y=5)

        # create category labels
        category1 = ctk.CTkLabel(window, text="Personal Information", font=("FixedSys", 15))
        category1.place(x=5, y=30)
        category2 = ctk.CTkLabel(window, text="Emergency Contact", font=("FixedSys", 15))
        category2.place(x=5, y=240)

        # create variables
        first_name = ctk.StringVar()
        surname = ctk.StringVar()
        age = ctk.StringVar()
        gender = ctk.StringVar()
        email = ctk.StringVar()
        phone = ctk.StringVar()
        address = ctk.StringVar()
        contact_first_name = ctk.StringVar()
        contact_surname = ctk.StringVar()
        contact_phone = ctk.StringVar()
        contact_address = ctk.StringVar()
        relationship = ctk.StringVar()
        overseas_options = ctk.StringVar(value="No")
        country_traveled = ctk.StringVar()

        # create labels for personal info
        personal_info_frame = ctk.CTkFrame(window, width=480, height=180, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        personal_info_frame.place(x=10, y=55)
        first_name_lbl = ctk.CTkLabel(window, text="First Name", font=("FixedSys", 12), text_color="dodger blue")
        first_name_lbl.place(x=15, y=60)
        surname_lbl = ctk.CTkLabel(window, text="Surname", font=("FixedSys", 12), text_color="dodger blue")
        surname_lbl.place(x=15, y=95)
        gender_lbl = ctk.CTkLabel(window, text="Gender", font=("FixedSys", 12), text_color="dodger blue")
        gender_lbl.place(x=250, y=60)
        age_lbl = ctk.CTkLabel(window, text="Age", font=("FixedSys", 12), text_color="dodger blue")
        age_lbl.place(x=270, y=95)
        email_lbl = ctk.CTkLabel(window, text="Email Address", font=("FixedSys", 12), text_color="dodger blue")
        email_lbl.place(x=15, y=130)
        phone_lbl = ctk.CTkLabel(window, text="Phone Number", font=("FixedSys", 12), text_color="dodger blue")
        phone_lbl.place(x=15, y=165)
        address_lbl = ctk.CTkLabel(window, text="Home Address", font=("FixedSys", 12), text_color="dodger blue")
        address_lbl.place(x=15, y=200)

        # create labels for emergency contact info
        personal_info_frame = ctk.CTkFrame(window, width=480, height=180, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        personal_info_frame.place(x=10, y=265)
        contact_first_name_lbl = ctk.CTkLabel(window, text="First Name", font=("FixedSys", 12), text_color="dodger blue")
        contact_first_name_lbl.place(x=15, y=270)
        contact_surname_lbl = ctk.CTkLabel(window, text="Surname", font=("FixedSys", 12), text_color="dodger blue")
        contact_surname_lbl.place(x=15, y=305)
        contact_phone_lbl = ctk.CTkLabel(window, text="Phone Number", font=("FixedSys", 12), text_color="dodger blue")
        contact_phone_lbl.place(x=15, y=340)
        contact_address_lbl = ctk.CTkLabel(window, text="Home Address", font=("FixedSys", 12), text_color="dodger blue")
        contact_address_lbl.place(x=15, y=375)
        relationship_lbl = ctk.CTkLabel(window, text="Relationship", font=("FixedSys", 12), text_color="dodger blue")
        relationship_lbl.place(x=15, y=410)

        # create labels for other questions
        # for overseas travel question
        overseas_frame = ctk.CTkFrame(window, width=350, height=70, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        overseas_frame.place(x=500, y=55)
        overseas_travel_lbl = ctk.CTkLabel(window, text="Have you traveled outside the country \n for the last "
                                                        "two months?", font=("FixedSys", 12), text_color="dodger blue")
        overseas_travel_lbl.place(x=525, y=60)

        # for country traveled question
        travel_frame = ctk.CTkFrame(window, width=350, height=75, fg_color="transparent", border_width=1,
                                    border_color="dodger blue")
        travel_frame.place(x=500, y=130)
        travel_country_lbl = ctk.CTkLabel(window, text="If yes, please select country. \n If no, choose N/A.",
                                          font=("FixedSys", 12), text_color="dodger blue")
        travel_country_lbl.place(x=555, y=135)

        # for positive or symptomatic question
        travel_frame = ctk.CTkFrame(window, width=350, height=75, fg_color="transparent", border_width=1,
                                    border_color="dodger blue")
        travel_frame.place(x=500, y=130)
        travel_country_lbl = ctk.CTkLabel(window, text="If yes, please select country. \n If no, choose N/A.",
                                          font=("FixedSys", 12), text_color="dodger blue")
        travel_country_lbl.place(x=555, y=135)

        # create entry buttons for personal info
        first_name_entry = ctk.CTkEntry(window, textvariable=first_name)
        first_name_entry.place(x=100, y=60)
        surname_entry = ctk.CTkEntry(window, textvariable=surname)
        surname_entry.place(x=85, y=95)
        age_entry = ctk.CTkEntry(window, textvariable=age, width=40)
        age_entry.place(x=305, y=95)
        email_entry = ctk.CTkEntry(window, textvariable=email, width=175)
        email_entry.place(x=125, y=130)
        phone_entry = ctk.CTkEntry(window, textvariable=phone, width=175)
        phone_entry.place(x=120, y=165)
        address_entry = ctk.CTkEntry(window, textvariable=address, width=275)
        address_entry.place(x=120, y=200)

        # create entry buttons for emergency contact info
        contact_first_name_entry = ctk.CTkEntry(window, textvariable=contact_first_name)
        contact_first_name_entry.place(x=100, y=270)
        contact_surname_entry = ctk.CTkEntry(window, textvariable=contact_surname)
        contact_surname_entry.place(x=85, y=305)
        contact_phone_entry = ctk.CTkEntry(window, textvariable=contact_phone, width=175)
        contact_phone_entry.place(x=120, y=340)
        contact_address_entry = ctk.CTkEntry(window, textvariable=contact_address, width=275)
        contact_address_entry.place(x=120, y=375)
        relationship_entry = ctk.CTkEntry(window, textvariable=relationship)
        relationship_entry.place(x=120, y=410)

        gender_button = ctk.CTkSegmentedButton(window, values=["Male", "Female", "LGBTQIA+"], variable=gender)
        gender_button.set("Not specified")
        gender_button.place(x=305, y=60)

        overseas_yes = ctk.CTkRadioButton(window, text="Yes", variable=overseas_options, value="Yes")
        overseas_yes.place(x=600, y=95)
        overseas_no = ctk.CTkRadioButton(window, text="No", variable=overseas_options, value="No")
        overseas_no.place(x=690, y=95)

        travel_country = ctk.CTkOptionMenu(window, values=['N/A', 'Afghanistan', 'Aland Islands', 'Albania', 'Algeria',
                                                           'American Samoa', 'Andorra', 'Angola', 'Anguilla',
                                                           'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia',
                                                           'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
                                                           'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                                                           'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
                                                           'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island',
                                                           'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
                                                           'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
                                                           'Cayman Islands', 'Central African Republic', 'Chad',
                                                           'Chile', 'China', 'Cocos Islands', 'Colombia', 'Comoros',
                                                           'Congo, The Democratic Republic of the', 'Costa Rica',
                                                           'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic',
                                                           'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
                                                           'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Ethiopia',
                                                           'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon',
                                                           'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar',
                                                           'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
                                                           'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana',
                                                           'Haiti', 'Heard Island and McDonald Islands', 'Honduras',
                                                           'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia',
                                                           'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man',
                                                           'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan',
                                                           'Kazakhstan', 'Kenya', 'Kiribati', "Korea, North",
                                                           'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon',
                                                           'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                                                           'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar',
                                                           'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                                                           'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
                                                           'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro',
                                                           'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
                                                           'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
                                                           'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan',
                                                           'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
                                                           'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal',
                                                           'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda',
                                                           'Samoa', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
                                                           'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                                                           'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
                                                           'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan',
                                                           'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
                                                           'Taiwan', 'Tajikistan', 'Tanzania, United Republic of',
                                                           'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga',
                                                           'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                                                           'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                                                           'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
                                                           'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands, British',
                                                           'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia',
                                                           'Zimbabwe'], variable=country_traveled)

        travel_country.pack(padx=20, pady=10)
        travel_country.set("N/A")

        travel_country.place(x=600, y=170)

        note = "Please fill out this form to help us track your contact history. \n" \
               "All information collected shall remain confidential and will be used for safety purposes only."
        note_lbl = ctk.CTkLabel(window, text=note, font=("FixedSys", 12))
        note_lbl.place(x=15, y=470)

        enter_data = partial(Options.add_entry, first_name, surname, age, gender, email, phone, address,
                             contact_first_name, contact_surname, contact_phone, contact_address, relationship,
                             overseas_options, country_traveled)
        add_entry_button = ctk.CTkButton(window, text="Add Entry", command=enter_data)
        add_entry_button.place(x=350, y=500)

    @staticmethod
    def search_entry_window():
        root.withdraw()
        window2 = ctk.CTkToplevel(root)
        window2.geometry("300x300")
        window2.title("Search Entry")

        first_name = ctk.StringVar()
        surname = ctk.StringVar()

        first_name_lbl = ctk.CTkLabel(window2, text="First Name")
        first_name_lbl.place(x=15, y=60)
        surname_lbl = ctk.CTkLabel(window2, text="Surname")
        surname_lbl.place(x=15, y=95)

        first_name_entry = ctk.CTkEntry(window2, textvariable=first_name)
        first_name_entry.place(x=85, y=60)
        surname_entry = ctk.CTkEntry(window2, textvariable=surname)
        surname_entry.place(x=85, y=95)

        search_data = partial(Options.search_entry, first_name, surname)
        search_entry_button = ctk.CTkButton(window2, text="Search Entry", command=search_data)
        search_entry_button.place(x=85, y=150)


title_lbl = ctk.CTkLabel(root, text="CONTACT\nTRACING", font=("FixedSys", 35), text_color="dodger blue")
title_lbl.place(x=70, y=60)

add_button = ctk.CTkButton(root, text="ADD ENTRY", font=("FixedSys", 10), command=OptionsWindow.open_entry_window)
add_button.place(x=85, y=160)
search_button = ctk.CTkButton(root, text="SEARCH ENTRY", font=("FixedSys", 10), command=OptionsWindow.search_entry_window)
search_button.place(x=85, y=195)

root.mainloop()
