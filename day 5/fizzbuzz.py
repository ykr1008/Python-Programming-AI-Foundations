for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
        
        
a=["FizzBuzz" if i%3==0 and i%5==0
   else "Fizz" if i%3==0
   else "Buzz" if i%5==0
   else i
   for i in range(1,101)
   ]
print(a)


# The normal for loop is more readable because each condition is written on a separate line, 
# making the logic easier to follow and debug. Readability is more important than writing fewer 
# lines because code is written not only for computers but also for people who need to understand,
# maintain, and modify it later.