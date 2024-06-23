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


def get_user_input(prompt):


def confirm_name(email):


main()
