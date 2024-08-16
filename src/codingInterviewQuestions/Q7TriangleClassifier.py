"""Write a program that classifies a triangle based on its side lengths. Given three input values
representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal). Use an if-else statement to
classify the triangle."""


def tri_classifier(x1, x2, x3) -> str:
    if x1 <= 0 or x2 <= 0 or x3 <= 0:
        return 'invalid triangle'
    if x1 + x2 <= x3 or x1 + x3 <= x2 or x2 + x3 <= x1:
        return 'invalid triangle'
    if x1 == x2 == x3:
        return 'equilateral triangle'
    elif x1 == x2 or x1 == x3 or x2 == x3:
        return 'isosceles triangle'
    else:
        return 'scalene triangle'


# Initialize an empty list to store the input values
inputs = []

# Loop to get 3 inputs from the user
for i in range(3):
    # Prompt the user for input and convert it to an integer
    xi = int(input(f"Enter x {i + 1}: "))
    # Append the input value to the list
    inputs.append(xi)

# Print the list of inputs
print("The input numbers are:", inputs)

print(tri_classifier(inputs[0], inputs[1], inputs[2]))
