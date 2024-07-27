def main():
    user_data = {}
    email = get_user_input("Email: ")

    while email != '':
        name = confirm_name(email)
        user_data[email] = name
        email = get_user_input("Email: ")

    print("\nList of users:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


def extract_name(email):
    parts = email.split('@')[0].split('.')
    name = ' '.join(part.title() for part in parts)
    return name


def get_user_input(prompt):
    return input(prompt).strip()


def confirm_name(email):
    name_from_email = extract_name(email)
    response = get_user_input(f"Is your name {name_from_email}? (Y/n) ").lower()

    if response in ['y', '']:
        return name_from_email
    elif response == 'n':
        return get_user_input("Name: ").strip()
    else:
        print("Invalid input. Please enter Y or n.")
        return confirm_name(email)


main()
