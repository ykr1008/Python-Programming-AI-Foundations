
import csv
from pathlib import Path


def load_students(file_path):
    students = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for student in reader:
            name = student["name"].strip()
            marks = float(student["marks"])

            if name and 0 <= marks <= 100:
                students.append({
                    "name": name,
                    "marks": marks
                })

    return students
