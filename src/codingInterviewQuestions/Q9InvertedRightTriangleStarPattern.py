def inv_triangle(n: int):
    for i in range(n, 0, -1):
        print('* ' * i)


height = int(input('Enter the height of the inverted triangle:-'))
inv_triangle(height)
