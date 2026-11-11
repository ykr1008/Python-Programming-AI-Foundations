# Python Basics Traps — Prediction vs Actual Results

| No. | Prediction | Actual Result | Explanation |
|---:|---|---|---|
| 1 | `3, -3, 1, 1` | `3 -4 1 1` | Floor division (`//`) rounds down toward negative infinity, so `-7 // 2` equals `-4`, not `-3`. |
| 2 | `2.0, float` | `2.0 <class 'float'>` | The `/` operator returns a float in Python 3, even when the division gives a whole number. |
| 3 | `True` | `True` | Python's CPython implementation reuses the same integer object for `256` in this example, so `is` returns `True`. |
| 4 | `False` | `True` | CPython reuses the integer constant in this code, but identity comparisons for integers are implementation-dependent and should not be relied on. |
| 5 | `False` | `False` | Floating-point numbers cannot represent some decimal fractions exactly, so `0.1 + 0.2` is not exactly equal to `0.3`. |
| 6 | `2` | `2` | In Python, `True` is equivalent to integer `1` when converted using `int()`, so the result is `1 + 1 = 2`. |
| 7 | `True False` | `True False` | The lists contain equal values, so `==` returns `True`; they are separate objects, so `is` returns `False`. |
| 8 | `True False False False` | `False True False True` | Empty strings and lists are false, while non-empty strings and lists are true, even when their contents include `0`. |
| 9 | `ValueError` | `ValueError` | `int('10.5')` raises a `ValueError` because `int()` cannot directly convert a decimal-formatted string into an integer. |
| 10 | `TypeError` | `TypeError` (expected; run separately to verify) | `input()` returns a string, so adding the integer `5` to the string entered by the user raises a `TypeError`. Convert the input using `int()` first. |

## Unit Converter Test Results

**Valid input**

- Input: `32`
- Output: `Temperature in Fahrenheit: 89.6°F`
- Result: Passed

**Invalid input**

- Input: `abc`
- Error name: `ValueError`
- Error message: `could not convert string to float: 'abc'`
- Result: Expected error for this assignment

## Conclusion

This exercise helped me understand Python's floor division, floating-point precision, object identity, Boolean conversion, exceptions, and input type conversion. It also demonstrated why user input must be converted to the appropriate data type before performing arithmetic operations.