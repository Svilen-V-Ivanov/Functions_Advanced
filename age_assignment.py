def age_assignment(*args, **kwargs):
    names = {}
    for name in args:
        for key, value in kwargs.items():
            if name[0] == key:
                names[name] = value
    sorted_names = [f"{key} is {value} years old." for key, value in sorted(names.items(), key=lambda x: x[0])]
    return '\n'.join(sorted_names)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))