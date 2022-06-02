def even_odd(*args):
    command = args[-1]
    numbers = []
    parity = 0 if command == 'even' else 1
    for num in range(len(args) - 1):
        number = args[num]
        if number % 2 == parity:
            numbers.append(number)

    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))