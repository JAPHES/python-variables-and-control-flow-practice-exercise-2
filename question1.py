#   THIS IS a program to to print numbers in the range of 1 to 50 using for loop
for x in range (51):
    print(x)
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3== 0 and x % 5 == 0:
        print("FizzBuzz")

