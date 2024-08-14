"""Create a program that checks whether a given string is a palindrome.
A palindrome is a word or phrase that reads the same backward as forward (ignoring spaces, punctuation,
and capitalization). Use an if-else statement to determine if the string is a palindrome."""
"""
print("Enter a word to check for palindrome")
a = input()
b = a[::-1]
if a == b:
    print("The given input is a palindrome")
else:
    print("Not a palindrome")"""

"""From chatgpt"""


def is_palindrome(s):
    """Checks if a given string is a palindrome."""

    # Remove spaces and punctuation, and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False


# Test cases
string1 = "A man, a plan, a canal: Panama"
string2 = "racecar"
string3 = "hello"

print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: True
print(is_palindrome(string3))  # Output: False  
