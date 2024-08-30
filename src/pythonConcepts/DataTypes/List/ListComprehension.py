"""List Comprehension
Python List comprehensions are used for creating new lists from other iterables like tuples,
strings, arrays, lists, etc. A list comprehension consists of brackets containing the expression,
which is executed for each element along with the for loop to iterate over each element.

Syntax:

newList = [ expression(element) for element in oldList if condition ]"""

# Python program to demonstrate list
# comprehension in Python

# below list contains square of all
# odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

