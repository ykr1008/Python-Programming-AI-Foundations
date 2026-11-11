
print(7 // 2, -7 // 2, 7 % 2, -7 % 2)
print(4 / 2, type(4 / 2))

x = 256
y = 256
print(x is y)

x = 257
y = 257
print(x is y)

print(0.1 + 0.2 == 0.3)
print(int(True) + int(True))

a = [1, 2]
b = [1, 2]
print(a == b, a is b)

print(bool(''), bool('0'), bool([]), bool([0]))

# print(int('10.5'))

age = input('Age: ')
print(age + 5)
