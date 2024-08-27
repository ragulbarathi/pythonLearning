"""Continue in Python For Loop
Python continue Statement returns the control to the beginning of the loop."""
# Prints all letters except 'e' and 's'

for letter in 'geeksforgeeks':

    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)