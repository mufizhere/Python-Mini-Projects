# 4. Password Manager

import secrets
import string

passwords = {}


def load_file():
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                parts = line.rstrip("\n").split(":", 1)

                if len(parts) != 2:
                    continue

                website, password = parts
                passwords[website] = password

    except FileNotFoundError:
        pass


def save_file():
    with open("passwords.txt", "w") as file:
        for website, password in passwords.items():
            file.write(f"{website} : {password}\n")


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def add_password():
    website = input("\nEnter Website Name: ").strip().lower()

    if not website:
        print("Website name cannot be empty.")
        return

    password = input("Enter Password: ").strip()

    if not password:
        print("Password cannot be empty.")
        return

    passwords[website] = password
    save_file()

    print("Password saved successfully!")


def view_password():
    if not passwords:
        print("No passwords found.")
        return

    print("\n----- Saved Passwords -----")

    for website, password in passwords.items():
        print(f"Website: {website}")
        print(f"Password: {password}")
        print("-" * 50)


def update_password():
    website = input("\nEnter Website Name: ").strip().lower()

    if website not in passwords:
        print("Website not found.")
        return

    new_password = input("Enter New Password: ").strip()

    if not new_password:
        print("Password cannot be empty.")
        return

    passwords[website] = new_password
    save_file()

    print("Password updated successfully!")


def delete_password():
    website = input("\nEnter Website Name To Delete Password: ").strip().lower()

    if website not in passwords:
        print("Website not found.")
        return

    del passwords[website]

    save_file()
    print("Password deleted successfully!")


def main():
    load_file()

    while True:
        print("\n----- Password Manager -----")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. View Passwords")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Exit\n")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                length = int(input("Enter Password Length (minimum 1): "))

                if length < 1:
                    print("Password length must be at least 1.")
                    continue

                password = generate_password(length)
                print(f"Generated Password: {password}")

                save_choice = input("\nDo you want to save this password? (yes/no): ").strip().lower()

                if save_choice == "yes" or "y":
                    website = input("Enter Website Name: ").strip().lower()

                    if not website:
                        print("Website name cannot be empty.")
                        continue

                    passwords[website] = password
                    save_file()

                    print("Generated password saved successfully!")

            except ValueError:
                print("Invalid length. Please enter a number.")

        elif choice == 2:
            add_password()

        elif choice == 3:
            view_password()

        elif choice == 4:
            update_password()

        elif choice == 5:
            delete_password()

        elif choice == 6:
            print("Thank you for using Password Manager!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
