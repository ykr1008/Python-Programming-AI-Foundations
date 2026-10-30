
from pathlib import Path

from student_report.loader import load_students

from student_report.analysis import (
    calculate_average,
    calculate_highest,
    calculate_lowest,
    count_passed,
    count_failed
)

from student_report.formatting import format_report


def main():
    csv_file = Path("students.csv")

    students = load_students(csv_file)

    marks = [student["marks"] for student in students]

    average = calculate_average(marks)
    highest = calculate_highest(marks)
    lowest = calculate_lowest(marks)
    passed = count_passed(marks)
    failed = count_failed(marks)

    report = format_report(
        students,
        average,
        highest,
        lowest,
        passed,
        failed
    )

    print(report)


if __name__ == "__main__":
    main()
