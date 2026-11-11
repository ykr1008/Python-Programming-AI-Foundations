
import random

a = random.randint(1, 100)
i = 0

for i in range(7):
    b = input("Guess a number (1-100): ")

    if not b.isdigit():
        print("Invalid input! Enter digits only.")
        continue

    b = int(b)

    if b == a:
        print("Correct! You won!")
        break
    elif b < a:
        print("Higher!")
    else:
        print("Lower!")
else:
    print(f"You lost! The number was {a}.")

    