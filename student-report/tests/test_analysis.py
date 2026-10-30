
from student_report.analysis import (
    calculate_average,
    calculate_highest,
    calculate_lowest,
    count_passed,
    count_failed
)


assert calculate_average([2, 4]) == 3
assert calculate_highest([10, 20, 30]) == 30
assert calculate_lowest([10, 20, 30]) == 10
assert count_passed([80, 30, 60]) == 2
assert count_failed([80, 30, 60]) == 1

print("All analysis tests passed!")
