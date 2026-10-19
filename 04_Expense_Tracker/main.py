# 5. Expense Tracker


expenses = []


def load_file():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("|")
                if len(parts) != 5:
                    continue

                try:
                    amount = float(parts[4].strip())
                except ValueError:
                    continue

                expenses.append({
                    "ids": parts[0].strip(),
                    "date": parts[1].strip(),
                    "category": parts[2].strip().lower(),
                    "description": parts[3].strip().lower(),
                    "amount": amount
                })
    except FileNotFoundError:
        pass


def save_file():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['ids']} | {expense['date']} | "
                f"{expense['category']} | {expense['description']} | "
                f"{expense['amount']}\n"
            )


def print_expense(expense):
    print(
        f"{expense['ids']} | {expense['date']} | "
        f"{expense['category']} | {expense['description']} | "
        f"{expense['amount']:.2f}"
    )


load_file()

while True:
    print("\n----- EXPENSE TRACKER -----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. View Total Expenses")
    print("7. Category-Wise Summary")
    print("8. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input. Please Enter a Valid Number.")
        continue


    # Add Expense
    if choice == 1:
        expense_id = input("Enter Expense ID: ").strip()

        if any(expense["ids"] == expense_id for expense in expenses):
            print("Error: Expense ID Already Exists.\n")
            continue

        date = input("Enter Expense Date: ").strip()
        category = input("Enter Expense Category: ").strip().lower()
        description = input("Enter Expense Description: ").strip().lower()

        try:
            amount = float(input("Enter Expense Amount: "))
        except ValueError:
            print("Invalid amount.")
            continue

        expenses.append({
            "ids": expense_id,
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })

        save_file()
        print("\nExpense Added Successfully!\n")


    # View All Expenses
    elif choice == 2:
        if not expenses:
            print("No Expense Found.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(f"\n{index}. ", end="")
                print_expense(expense)


    # Search Expense
    elif choice == 3:
        if not expenses:
            print("No Expense Found.")
            continue

        search_id = input("Enter ID to Search Expense: ").strip()
        found = False

        for expense in expenses:
            if expense["ids"] == search_id:
                print_expense(expense)
                found = True
                break

        if not found:
            print("ID Not Found.")


    # Update Expense
    elif choice == 4:
        if not expenses:
            print("No Expense Found")
            continue

        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. ", end="")
            print_expense(expense)

        update_ids = input("\nEnter ID To Update The Expense: ").strip()

        found = False

        for expense in expenses:
            if expense["ids"] == update_ids:
                found = True

                print("1. Update Date")
                print("2. Update Category")
                print("3. Update Description")
                print("4. Update Amount")
                print("5. Exit")

                try:
                    update_choice = int(input("Enter Update Choice: "))
                except ValueError:
                    print("Invalid Choice.")
                    break

                if update_choice == 1:
                    new_date = input(f"New Date [{expense['date']}]: ").strip()
                    if new_date:
                        expense["date"] = new_date
                    print("\nDate Updated Successfully!")

                elif update_choice == 2:
                    new_category = input(f"New Category [{expense['category']}]: ").strip().lower()
                    if new_category:
                        expense["category"] = new_category
                    print("\nCategory Updated Successfully!")

                elif update_choice == 3:
                    new_description = input(
                        f"New Description [{expense['description']}]: ").strip().lower()
                    if new_description:
                        expense["description"] = new_description
                    print("\nDescription Updated Successfully!")

                elif update_choice == 4:
                    new_amount = input(f"New Amount [{expense['amount']}]: ").strip()
                    try:
                        expense["amount"] = float(new_amount)
                        print("\nAmount Updated Successfully!")
                    except ValueError:
                        print("Invalid Amount; Amount Not Updated.")

                elif update_choice == 5:
                    print("Update cancelled.")
                    break

                else:
                    print("Invalid Choice. Try Again.")
                    break

                save_file()
                break

        if not found:
            print("ID Not Found.")


    # Delete Expense
    elif choice == 5:
        if not expenses:
            print("No Expense Found.")
            continue

        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. ", end="")
            print_expense(expense)
        
        delete_id = input("\nEnter ID To Delete Expense: ").strip()

        for index, expense in enumerate(expenses):
            if expense["ids"] == delete_id:
                deleted_expense = expense.pop(index)
                save_file()
                print_expense(deleted_expense)
                print("Expense Delete Successfully!")
                break
        else:
            print("ID not Found")            


    # View Total Expenses
    elif choice == 6:
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expenses: {total:.2f}")


    # Category-Wise Summary
    elif choice == 7:
        if not expenses:
            print("Noo Expense Found")
            continue

        summary = {}
        for expense in expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]

        for category, total in summary.items():
            print(f"{category}: {total:.2f}")


    # Exit
    elif choice == 8:
        print("Thank You For Using Expense Tracker!!!")
        break

    else:
        print("Invalid Choice. Please Choose (1-8)")