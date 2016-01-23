def add_arguments(*args):
    total=0
    for a in args:
        total += a
    print(total)

add_arguments(3)
add_arguments(1, 2, 3, 4, 5)
add_arguments(100, 200, 354, 8763482)
