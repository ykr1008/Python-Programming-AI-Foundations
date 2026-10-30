
import csv
from pathlib import Path


def main():
    csv_file = Path("students.csv")

    # Read the CSV file.
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    # Clean the data and convert marks to numbers.
    cleaned_students = []

    for student in students:
        name = student["name"].strip()
        marks = float(student["marks"])

        if name and 0 <= marks <= 100:
            cleaned_students.append({
                "name": name,
                "marks": marks
            })

    # Calculate statistics.
    marks_list = [student["marks"] for student in cleaned_students]

    if not marks_list:
        print("No valid student records found.")
        return

    average = sum(marks_list) / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)
    passed = sum(1 for mark in marks_list if mark >= 40)

    # Print the report.
    print("STUDENT REPORT")
    print("=" * 30)
    print(f"Students: {len(cleaned_students)}")
    print(f"Average: {average:.2f}")
    print(f"Highest mark: {highest:.2f}")
    print(f"Lowest mark: {lowest:.2f}")
    print(f"Passed: {passed}")
    print(f"Failed: {len(marks_list) - passed}")


if __name__ == "__main__":
    main()
