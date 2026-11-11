# 1. Reverse the words in a sentence.
word="the sky is blue"
w=(word.split()[::-1])
w1=" ".join(w)
print(w1)

# 2. Check whether a sentence is a palindrome, ignoring case and spaces.
a="Never odd or even"
b=a.lower()
c="".join(b.split())
print(c==c[::-1])

# 3. Count how many times a character appears in a sentence
a=input("Enter something: ")
print(a.count(input("enter the character to count: ")))

# 4. Check whether one string is a rotation of another.
a="waterbottle"
b=a+a
c="erbottlewat"
print(len(a)==len(c) and c in b)

# 5. Tidy a name by removing extra spaces and capitalizing each word.
a="john smith"
b=(a.strip()).title()
print(b)

# 6. Mask an email address, showing the first username character.
a="john.smith@gmail.com"
b=a.split("@")
print(f"{b[0][0]}***@{b[1]}")

# 7. Count vowels without using a loop.
a=(input("Enter: ")).lower()
b=a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")
print(b)

# 8. Format a receipt line to exactly 26 characters using an f-string.
item=input("enter item: ")
price=float(input("enter price: "))
print(f"{item:.<{26-len(f'{price:.2f}')}}{price:.2f}")