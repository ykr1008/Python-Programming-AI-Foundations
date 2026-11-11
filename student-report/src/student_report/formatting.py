
def format_report(students, average, highest, lowest, passed, failed):
    report = [
        "STUDENT REPORT",
        "=" * 30,
        f"Students: {len(students)}",
        f"Average: {average:.2f}",
        f"Highest mark: {highest:.2f}",
        f"Lowest mark: {lowest:.2f}",
        f"Passed: {passed}",
        f"Failed: {failed}"
    ]

    return "\n".join(report)
