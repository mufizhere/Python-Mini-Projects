# 1. Simple Calculator

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
        return num1 / num2

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid Choice, Please Try Again")

    elif choice == 1:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter second Number: "))

        result = addition(num1, num2)
        print(f"\nAddition: {result}")

    elif  choice == 2:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter second Number: "))

        result = subtraction(num1, num2)
        print(f"\nSubtraction: {result}")

    elif choice == 3:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        result = multiplication(num1, num2)
        print(f"\nMultiplication: {result}")

    elif choice == 4:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if num2 == 0:
            print("\nDivision by zero is not defined.")
        else:
            result = num1 / num2
            print(F"\nDivision: {result}")

    elif choice == 5:
        print('Thank You for Using Calculator')
        break