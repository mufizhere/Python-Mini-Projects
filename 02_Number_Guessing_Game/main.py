# 2. Number Guessing Game

import random

computer = random.randint(1, 100)
ATTEMPTS = 10

print("\n----- Walcome To Number Guessing Game -----")
print("You Have Only 10 Attempt to Guess A Number\n")

while ATTEMPTS > 0:

    user = int(input("Guess Number Between 1 to 100: "))

    ATTEMPTS -= 1
    remaining_attempts = ATTEMPTS

    if ATTEMPTS == 0:
        print("\nYou Lose!")
        print("Better Luck Next Time!")
        print("Please Try Again.")

    elif user < computer:
        print("\nToo Low!")
        print(f"You have {remaining_attempts} Attempts Left.\n")

    elif user > computer:
        print("\nToo High!")
        print(f"You have {remaining_attempts} Attempts Left.\n")

    else:
        print("\nYou Won!")
        print("Congratulations!")
        print(f"Number Was '{computer}'")
        break