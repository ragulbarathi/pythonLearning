"""Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
based on the following grading scale:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""


def gradecalculator(n):
    if n <= 59:
        print("F")
    elif 59 < n <= 69:
        print('D')
    elif 69 < n <= 79:
        print("C")
    elif 79 < n <= 89:
        print("B")
    else:
        print('A')


print("Grade calculator")
print('Enter your marks')
gradecalculator(int(input()))
