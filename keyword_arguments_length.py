def kwargs_length(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        dict[key] = value

    return len(dict)



dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

dictionary = {}

print(kwargs_length(**dictionary))