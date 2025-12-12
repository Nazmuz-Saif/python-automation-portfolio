# def info(name,  phone, email):
#     contact  = {"name": name, "phone": phone, "email": email}
#
#     with open('contacts.txt', 'a') as file:
#         file.write(contact.__str__())
#         file.write('\n')

def add_contact():
    name = input('Enter your name: ')
    phone = input('Enter your phone number: ')
    email = input('Enter your email: ')
    # info(name, phone, email)
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print('Contact added')


def view_contact():
    try:
        with open('contacts.txt', 'r') as file:
            #contact = {}
            contact = file.readlines()

        if len(contact) == 0:
            print('There are no contacts')
        else:
            print('---Contact List---')
            # print(contact)
            for i, contact in enumerate(contact, 1):
                name, phone, email = contact.split(",")
                print(f"{i}. {name} | {phone} | {email}")

    except FileNotFoundError:
        print('No contacts yet')


def search_contact():
    names = input('Enter name: ').lower()
    try:
        with open('contacts.txt', 'r') as file:
            contact = file.readlines()

        found = False
        for cnt in contact:
            name, phone, email = cnt.split(",")
            if names == name.lower():
                print(f'Name: {name}, Phone: {phone}, Email: {email}')
                found = True
        if not found:
            print('No contacts found')

    except FileNotFoundError:
        print('No contacts yet')

def delete_contact():
    names = input('Enter name: ').lower()
    try:
        with open('contacts.txt', 'r') as file:
            contact = file.readlines()

        # list = []
        new_list = []
        deletee = False

        for i in contact:
            name, phone, email = i.split(",")
            if names != name.lower():
                new_list.append(i)
            else:
                deletee = True
                print(f'Deleted: {name}')

        if deletee:
            with open('contacts.txt', 'w') as file:
                file.writelines(new_list)
        else:
            print('No contacts found')

    except FileNotFoundError:
        print('No contacts yet')


while True:
    print("---Contact Manager---")

    print('1. Add Contact')
    print('2. View Contact')
    print('3. Search Contact')
    print('4. Delete Contact')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print('tata bye bye')
        break
    else:
        print('Invalid choice')