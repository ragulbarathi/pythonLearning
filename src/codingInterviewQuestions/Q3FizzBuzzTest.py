"""FizzBuzz Test:
Write a program that prints numbers from 1 to 100. However, for multiples of 3,
print "Fizz" instead of the number, and for multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""


def fizzbuzz(n):
    for num in range(1, n + 1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizzbuzz(100)
