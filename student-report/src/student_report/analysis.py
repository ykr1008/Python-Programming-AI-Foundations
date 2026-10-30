
def calculate_average(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


def calculate_highest(marks):
    if not marks:
        return 0

    return max(marks)


def calculate_lowest(marks):
    if not marks:
        return 0

    return min(marks)


def count_passed(marks):
    return sum(1 for mark in marks if mark >= 40)


def count_failed(marks):
    return sum(1 for mark in marks if mark < 40)
