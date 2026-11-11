
from datetime import datetime


def add_note():
    note = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {note}\n")

    print("Note saved.")


def read_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            print("\n--- Your Notes ---")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("No notes found yet. Add your first note!")


def main():
    while True:
        print("\n1. Add a note")
        print("2. Read notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()


# 1. Why use with instead of calling close() yourself?
# The with statement automatically closes a file when its block ends, even if an exception occurs. 
# This makes file handling safer and cleaner than calling close() manually, which might be forgotten 
# or skipped if an error happens.
# 2. What is the difference between ValueError and TypeError?
# A ValueError occurs when an operation receives the correct type of value but the value itself is 
# invalid, such as int("hello"). A TypeError occurs when an operation receives an inappropriate type, 
# such as trying to add a string and an integer with "5" + 2.