# import modules
import customtkinter as ctk
from functools import partial
from program_code import Options

# change theme to dark
ctk.set_appearance_mode("dark")

# create method
root = ctk.CTk()
root.geometry("300x300+500+150")
root.title("Contact Tracing App")


class OptionsWindow:
    @staticmethod
    def open_entry_window():
        # new window
        add_window = ctk.CTkToplevel(root)
        add_window.geometry("875x600+250+50")
        add_window.title("Add Entry")
        root.withdraw()

        # create label for title
        title = ctk.CTkLabel(add_window, text="CONTACT TRACING", font=("FixedSys", 30), text_color="dodger blue")
        title.place(x=300, y=5)

        # create category labels
        category1_lbl = ctk.CTkLabel(add_window, text="Personal Information", font=("FixedSys", 15))
        category1_lbl.place(x=5, y=30)
        category2_lbl = ctk.CTkLabel(add_window, text="Emergency Contact", font=("FixedSys", 15))
        category2_lbl.place(x=5, y=240)
        category3_lbl = ctk.CTkLabel(add_window, text="Recent Contacts", font=("FixedSys", 15), text_color="white")
        category3_lbl.place(x=500, y=305)

        # create variables
        first_name = ctk.StringVar()
        surname = ctk.StringVar()
        age = ctk.StringVar()
        gender = ctk.StringVar()
        email = ctk.StringVar()
        phone = ctk.StringVar()
        address = ctk.StringVar()
        emergency_contact_first_name = ctk.StringVar()
        emergency_contact_surname = ctk.StringVar()
        emergency_contact_phone = ctk.StringVar()
        emergency_contact_address = ctk.StringVar()
        relationship = ctk.StringVar()
        overseas_options = ctk.StringVar(value="No")
        country_traveled = ctk.StringVar()
        situation_options = ctk.StringVar(value="Diagnosed with Coronavirus")
        recent_contact_name = ctk.StringVar()
        recent_contact_address = ctk.StringVar()
        recent_contact_date = ctk.StringVar()
        more_contact_name = ctk.StringVar()
        more_contact_address = ctk.StringVar()
        more_contact_date = ctk.StringVar()

        # create labels for personal info
        personal_info_frame = ctk.CTkFrame(add_window, width=480, height=180, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        personal_info_frame.place(x=10, y=55)
        first_name_lbl = ctk.CTkLabel(add_window, text="First Name", font=("FixedSys", 12), text_color="dodger blue")
        first_name_lbl.place(x=15, y=60)
        surname_lbl = ctk.CTkLabel(add_window, text="Surname", font=("FixedSys", 12), text_color="dodger blue")
        surname_lbl.place(x=15, y=95)
        gender_lbl = ctk.CTkLabel(add_window, text="Gender", font=("FixedSys", 12), text_color="dodger blue")
        gender_lbl.place(x=250, y=60)
        age_lbl = ctk.CTkLabel(add_window, text="Age", font=("FixedSys", 12), text_color="dodger blue")
        age_lbl.place(x=270, y=95)
        email_lbl = ctk.CTkLabel(add_window, text="Email Address", font=("FixedSys", 12), text_color="dodger blue")
        email_lbl.place(x=15, y=130)
        phone_lbl = ctk.CTkLabel(add_window, text="Phone Number", font=("FixedSys", 12), text_color="dodger blue")
        phone_lbl.place(x=15, y=165)
        address_lbl = ctk.CTkLabel(add_window, text="Home Address", font=("FixedSys", 12), text_color="dodger blue")
        address_lbl.place(x=15, y=200)

        # create labels for emergency contact info
        personal_info_frame = ctk.CTkFrame(add_window, width=480, height=180, fg_color="transparent", border_width=1,
                                           border_color="dodger blue")
        personal_info_frame.place(x=10, y=265)
        emergency_contact_first_name_lbl = ctk.CTkLabel(add_window, text="First Name", font=("FixedSys", 12), text_color="dodger blue")
        emergency_contact_first_name_lbl.place(x=15, y=270)
        emergency_contact_surname_lbl = ctk.CTkLabel(add_window, text="Surname", font=("FixedSys", 12), text_color="dodger blue")
        emergency_contact_surname_lbl.place(x=15, y=305)
        emergency_contact_phone_lbl = ctk.CTkLabel(add_window, text="Phone Number", font=("FixedSys", 12), text_color="dodger blue")
        emergency_contact_phone_lbl.place(x=15, y=340)
        emergency_contact_address_lbl = ctk.CTkLabel(add_window, text="Home Address", font=("FixedSys", 12), text_color="dodger blue")
        emergency_contact_address_lbl.place(x=15, y=375)
        relationship_lbl = ctk.CTkLabel(add_window, text="Relationship", font=("FixedSys", 12), text_color="dodger blue")
        relationship_lbl.place(x=15, y=410)

        # create labels for recent contact
        recent_contact_frame = ctk.CTkFrame(add_window, width=350, height=115, fg_color="transparent", border_width=1, border_color="dodger blue")
        recent_contact_frame.place(x=500, y=330)
        recent_contact_name_lbl = ctk.CTkLabel(add_window, text="Name", font=("FixedSys", 12), text_color="dodger blue")
        recent_contact_name_lbl.place(x=520, y=340)
        recent_contact_address_lbl = ctk.CTkLabel(add_window, text="Address", font=("FixedSys", 12), text_color="dodger blue")
        recent_contact_address_lbl.place(x=520, y=375)
        recent_contact_date_lbl = ctk.CTkLabel(add_window, text="Date of Contact", font=("FixedSys", 12), text_color="dodger blue")
        recent_contact_date_lbl.place(x=520, y=410)

        # for overseas travel question
        overseas_frame = ctk.CTkFrame(add_window, width=350, height=70, fg_color="transparent", border_width=1, border_color="dodger blue")
        overseas_frame.place(x=500, y=55)
        overseas_travel_lbl = ctk.CTkLabel(add_window, text="Have you traveled outside the country \n for the last "
                                                        "two months?", font=("FixedSys", 12), text_color="dodger blue")
        overseas_travel_lbl.place(x=525, y=60)

        # for country traveled question
        travel_frame = ctk.CTkFrame(add_window, width=350, height=75, fg_color="transparent", border_width=1,
                                    border_color="dodger blue")
        travel_frame.place(x=500, y=130)
        travel_country_lbl = ctk.CTkLabel(add_window, text="If yes, please select country. \n If no, choose N/A.",
                                          font=("FixedSys", 12), text_color="dodger blue")
        travel_country_lbl.place(x=555, y=135)

        # for positive or symptomatic question
        situation_frame = ctk.CTkFrame(add_window, width=350, height=95, fg_color="transparent", border_width=1,
                                      border_color="dodger blue")
        situation_frame.place(x=500, y=210)
        situation_lbl = ctk.CTkLabel(add_window, text="Please select the option that applies \n"
                                                  "to your situation", font=("FixedSys", 12), text_color="dodger blue")
        situation_lbl.place(x=525, y=215)

        # create entry/input boxes for personal info
        first_name_entry = ctk.CTkEntry(add_window, textvariable=first_name)
        first_name_entry.place(x=100, y=60)
        surname_entry = ctk.CTkEntry(add_window, textvariable=surname)
        surname_entry.place(x=85, y=95)
        age_entry = ctk.CTkEntry(add_window, textvariable=age, width=40)
        age_entry.place(x=305, y=95)
        email_entry = ctk.CTkEntry(add_window, textvariable=email, width=175)
        email_entry.place(x=125, y=130)
        phone_entry = ctk.CTkEntry(add_window, textvariable=phone, width=175)
        phone_entry.place(x=120, y=165)
        address_entry = ctk.CTkEntry(add_window, textvariable=address, width=275)
        address_entry.place(x=120, y=200)

        # create entry/input boxes for emergency contact info
        emergency_contact_first_name_entry = ctk.CTkEntry(add_window, textvariable=emergency_contact_first_name)
        emergency_contact_first_name_entry.place(x=100, y=270)
        emergency_contact_surname_entry = ctk.CTkEntry(add_window, textvariable=emergency_contact_surname)
        emergency_contact_surname_entry.place(x=85, y=305)
        emergency_contact_phone_entry = ctk.CTkEntry(add_window, textvariable=emergency_contact_phone, width=175)
        emergency_contact_phone_entry.place(x=120, y=340)
        emergency_contact_address_entry = ctk.CTkEntry(add_window, textvariable=emergency_contact_address, width=275)
        emergency_contact_address_entry.place(x=120, y=375)
        relationship_entry = ctk.CTkEntry(add_window, textvariable=relationship)
        relationship_entry.place(x=120, y=410)

        # create entry/input boxes for recent contact
        recent_contact_name_entry = ctk.CTkEntry(add_window, textvariable=recent_contact_name, width=215)
        recent_contact_name_entry.place(x=560, y=340)
        recent_contact_address_entry = ctk.CTkEntry(add_window, textvariable=recent_contact_address, width=245)
        recent_contact_address_entry.place(x=585, y=375)
        recent_contact_date_entry = ctk.CTkEntry(add_window, textvariable=recent_contact_date, width=155)
        recent_contact_date_entry.place(x=645, y=410)

        # make a button for gender
        gender_button = ctk.CTkSegmentedButton(add_window, values=["Male", "Female", "LGBTQIA+"], variable=gender)
        gender_button.set("Not specified")
        gender_button.place(x=305, y=60)

        # make buttons for options (yes or no) in overseas travel question
        overseas_yes = ctk.CTkRadioButton(add_window, text="Yes", variable=overseas_options, value="Yes")
        overseas_yes.place(x=600, y=95)
        overseas_no = ctk.CTkRadioButton(add_window, text="No", variable=overseas_options, value="No")
        overseas_no.place(x=690, y=95)

        # make a selection for countries traveled
        travel_country = ctk.CTkOptionMenu(add_window, values=['N/A', 'Afghanistan', 'Aland Islands', 'Albania',
                                                               'Algeria', 'American Samoa', 'Andorra', 'Angola',
                                                               'Anguilla', 'Antarctica', 'Antigua and Barbuda',
                                                               'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
                                                               'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
                                                               'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
                                                               'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
                                                               'Botswana', 'Bouvet Island','Brazil', 'Brunei', 'Bulgaria',
                                                               'Burkina Faso', 'Burundi','Cambodia', 'Cameroon', 'Canada',
                                                               'Cape Verde', 'Cayman Islands', 'Central African Republic',
                                                               'Chad', 'Chile', 'China', 'Cocos Islands', 'Colombia',
                                                               'Comoros', 'Congo, The Democratic Republic of the',
                                                               'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
                                                               'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
                                                               'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Ethiopia',
                                                               'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon',
                                                               'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar',
                                                               'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
                                                               'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau',
                                                               'Guyana', 'Haiti', 'Heard Island and McDonald Islands',
                                                               'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India',
                                                               'Indonesia', 'Iran, Islamic Republic of', 'Iraq',
                                                               'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica',
                                                               'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
                                                               'Kiribati', "Korea, North", 'Korea, South', 'Kuwait',
                                                               'Kyrgyzstan', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
                                                               'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                                                               'Macao', 'Macedonia, Republic of', 'Madagascar',
                                                               'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                                                               'Martinique', 'Mauritania', 'Mauritius', 'Mayotte',
                                                               'Mexico', 'Moldova, Republic of', 'Monaco', 'Mongolia',
                                                               'Montenegro', 'Montserrat', 'Morocco', 'Mozambique',
                                                               'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
                                                               'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger',
                                                               'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau',
                                                               'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
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
                                                               'Venezuela', 'Vietnam', 'Virgin Islands, British',
                                                               'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen',
                                                               'Zambia','Zimbabwe'], variable=country_traveled)

        travel_country.pack(padx=20, pady=10)
        travel_country.set("N/A")
        travel_country.place(x=600, y=170)

        # make options for situation (positive or symptomatic) question
        option1 = "Diagnosed with Coronavirus"
        option2 = "Shows symptoms of Coronavirus"
        situation_option1 = ctk.CTkRadioButton(add_window, text=option1, variable=situation_options, value=option1)
        situation_option1.place(x=550, y=250)
        situation_option2 = ctk.CTkRadioButton(add_window, text=option2, variable=situation_options, value=option2)
        situation_option2.place(x=550, y=275)

        # add additional pop-up window for more contacts
        def add_contact_window():
            contact_window = ctk.CTkToplevel(add_window)
            contact_window.title("Add Contact")
            contact_window.geometry("400x200+500+150")
            contact_window.attributes('-topmost', 'true')

            # create labels for additional contact name, address, date of contact
            add_contact_lbl = ctk.CTkLabel(contact_window, text="ADD CONTACT", font=("FixedSys", 25), text_color="white")
            add_contact_lbl.place(x=105, y=0)
            more_contact_name_lbl = ctk.CTkLabel(contact_window, text="Name", font=("FixedSys", 12), text_color="dodger blue")
            more_contact_name_lbl.place(x=15, y=40)
            more_contact_address_lbl = ctk.CTkLabel(contact_window, text="Address", font=("FixedSys", 12), text_color="dodger blue")
            more_contact_address_lbl.place(x=15, y=75)
            more_contact_date_lbl = ctk.CTkLabel(contact_window, text="Date of Contact", font=("FixedSys", 12), text_color="dodger blue")
            more_contact_date_lbl.place(x=15, y=110)

            # create entry/input boxes for additional contact name, address, date of contact
            more_contact_name_entry = ctk.CTkEntry(contact_window, textvariable=more_contact_name, width=200)
            more_contact_name_entry.place(x=90, y=40)
            more_contact_address_entry = ctk.CTkEntry(contact_window, textvariable=more_contact_address, width=275)
            more_contact_address_entry.place(x=90, y=75)
            more_contact_date_entry = ctk.CTkEntry(contact_window, textvariable=more_contact_date, width=175)
            more_contact_date_entry.place(x=140, y=110)

            # make a button to add additional information
            enter_contact_data = partial(Options.additional_contact, first_name, surname, more_contact_name,
                                         more_contact_address, more_contact_date)
            add_more_contact = ctk.CTkButton(contact_window, text="Add", command=enter_contact_data)
            add_more_contact.place(x=118, y=150)

        # add a note indicating confidentiality
        note = "Please fill out this form to help us track your contact history. \n" \
               "All information collected shall remain confidential and will be used for safety purposes only."
        note_lbl = ctk.CTkLabel(add_window, text=note, font=("FixedSys", 12))
        note_lbl.place(x=50, y=470)

        # create function for return button
        def return_to_first_window():
            add_window.destroy()
            root.deiconify()

        # make buttons for data entry, additional contact entry, return
        enter_data = partial(Options.add_entry, first_name, surname, age, gender, email, phone, address,
                             emergency_contact_first_name, emergency_contact_surname, emergency_contact_phone,
                             emergency_contact_address, relationship,overseas_options, country_traveled,
                             situation_options, recent_contact_name,recent_contact_address, recent_contact_date)
        add_entry_button = ctk.CTkButton(add_window, text="Add Entry", font=("FixedSys", 10), command=enter_data)
        add_entry_button.place(x=350, y=520)
        add_contact = ctk.CTkButton(add_window, text="Add More Contacts", font=("FixedSys", 10), command=add_contact_window)
        add_contact.place(x=500, y=520)
        return_button = ctk.CTkButton(add_window, text="Back", font=("FixedSys", 10), command=return_to_first_window)
        return_button.place(x=200, y=520)

    # create window for search entry
    @staticmethod
    def search_entry_window():
        root.withdraw()
        search_window = ctk.CTkToplevel(root)
        search_window.geometry("300x300+500+150")
        search_window.title("Search Entry")

        # create needed variables
        first_name = ctk.StringVar()
        surname = ctk.StringVar()

        # create title label
        search_lbl = ctk.CTkLabel(search_window, text="SEARCH ENTRY", font=("FixedSys", 25), text_color="white")
        search_lbl.place(x=60, y=50)

        # create labels for variables
        first_name_lbl = ctk.CTkLabel(search_window, text="First\nName", font=("FixedSys", 15), text_color="dodger blue")
        first_name_lbl.place(x=40, y=110)
        surname_lbl = ctk.CTkLabel(search_window, text="Surname", font=("FixedSys", 15), text_color="dodger blue")
        surname_lbl.place(x=25, y=145)

        # create entry/input boxes for first name and surname
        first_name_entry = ctk.CTkEntry(search_window, textvariable=first_name)
        first_name_entry.place(x=85, y=110)
        surname_entry = ctk.CTkEntry(search_window, textvariable=surname)
        surname_entry.place(x=85, y=145)

        # create function for return button
        def return_to_first_window():
            search_window.destroy()
            root.deiconify()

        # make search entry and return buttons
        search_data = partial(Options.search_entry, first_name, surname)
        search_entry_button = ctk.CTkButton(search_window, text="Search Entry", font=("FixedSys", 10), command=search_data)
        search_entry_button.place(x=85, y=220)
        return_button = ctk.CTkButton(search_window, text="Back", font=("FixedSys", 10), command=return_to_first_window)
        return_button.place(x=85, y=255)


# create a title label for the main window
title_lbl = ctk.CTkLabel(root, text="CONTACT\nTRACING", font=("FixedSys", 35), text_color="dodger blue")
title_lbl.place(x=70, y=60)

# make buttons for add and search entry options in main window
add_button = ctk.CTkButton(root, text="ADD ENTRY", font=("FixedSys", 10), command=OptionsWindow.open_entry_window)
add_button.place(x=85, y=160)
search_button = ctk.CTkButton(root, text="SEARCH ENTRY", font=("FixedSys", 10), command=OptionsWindow.search_entry_window)
search_button.place(x=85, y=195)

root.mainloop()
