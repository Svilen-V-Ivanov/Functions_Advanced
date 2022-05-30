def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


info_1 = {
    'name': 'Pesho',
    'town': 'Burgas',
    'age': 18,
}

info_2 = {
    'name': 'Gosho',
    'town': 'STara Zagora',
    'age': 48,
}

print(get_info(**info_1))
print(get_info(**info_2))
