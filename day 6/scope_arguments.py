

# 1. Modifying a list inside a function

def f(lst):
    lst.append(4)

a = [1, 2, 3]
f(a)
print(a)

# Prediction: [1, 2, 3, 4]
# Actual result: [1, 2, 3, 4]
# Explanation: append() modifies the original list because lst and a
# refer to the same list object.


# 2. Reassigning a function parameter

def g(lst):
    lst = [9, 9]

b = [1, 2, 3]
g(b)
print(b)

# Prediction: [1, 2, 3]
# Actual result: [1, 2, 3]
# Explanation: Reassigning lst to a new list does not change the list
# referenced by b outside the function.


# 3. Modifying a global variable

count = 0

def inc():
    count += 1

# Prediction: count becomes 1
# Actual result: UnboundLocalError
# Explanation: Python treats count as a local variable because the
# function assigns to it, but tries to read it before it has a value.

# Fix 1: Use the global keyword

count = 0

def inc():
    global count
    count += 1

inc()
print(count)

# Explanation: global count tells Python to modify the global variable.


# Fix 2: Pass the value and return the updated value

def inc(count):
    return count + 1

count = 0
count = inc(count)
print(count)

# Explanation: The function returns the incremented value without
# modifying a global variable.


# 4. Mutable default arguments

def add(x, target=[]):
    target.append(x)
    return target

print(add(1))
print(add(2))

# Prediction: [1] and [2]
# Actual result: [1] and [1, 2]
# Explanation: The default list is created once when the function
# is defined and reused across calls.

