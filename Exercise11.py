number = int(input())
for x in range(number):
    spaces = number - x - 1
    stars = 2 * x + 1
    print(" " * spaces + "*" * stars)