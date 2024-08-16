def pyramid_pattern(n: int):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("* " * i)


height = int(input('Enter height of pyramid:-'))
pyramid_pattern(height)

