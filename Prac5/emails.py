
email_to_fullname = {}
email = input('Email: ')
while email != '':
    name = email.split('@')[0]
    name = name.split('.')
    # print(name)
    fullname = ' '.join(name).title()
    # print(email)
    # print(fullname)
    confirmation = input(f"Is your name {fullname}? (Y/n) ")
    if confirmation.upper() == "N" and confirmation != "":
        fullname = input("Fullname: ")
    email_to_fullname[email] = fullname
    # print(email_to_fullname[email])
    # print(email_to_fullname)
    email = input('Email: ')

for email, fullname in email_to_fullname.items():
    print(f'{fullname} ({email})')
