def math_operations(*args, **kwargs):
    numbers = [float(x) for x in args]
    processes = {}
    for num in range(len(numbers)):
        for key, value in kwargs.items():
            if num % 4 == 0:
                kwargs['a'] += numbers[num]
            if num % 4 == 1:
                kwargs['s'] -= numbers[num]
            if num % 4 == 2:
                if numbers[num] != 0:
                    kwargs['d'] /= numbers[num]
            if num % 4 == 3:
                kwargs['m'] *= numbers[num]
            break

    sorted_list =[f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(sorted_list)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))