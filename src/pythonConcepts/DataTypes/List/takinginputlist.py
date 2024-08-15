# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list

# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split()
print('The list is:', lst)  # printing the list

'via Loops'
# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)

print(lst)
'via exception handling'
# try block to handle the exception
try:
    my_list = []

    while True:
        my_list.append(int(input()))

# if the input is not-integer, just print the list
except:
    print(my_list)
    'via Map'
# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int,
             input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", a)

'via List Comprehension and Type Casting'
# For list of integers
lst1 = []

# For list of strings/chars
lst2 = []

lst1 = [int(item) for item in input("Enter \the list items : ").split()]

lst2 = [item for item in input("Enter \the list items : ").split()]

print(lst1)
print(lst2)
