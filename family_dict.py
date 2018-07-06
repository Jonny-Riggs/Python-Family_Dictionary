my_family = {
    'father': {
        'name': 'Bill',
        'age': 52
    },
    'mother': {
        'name': 'Angie',
        'age': 50
    },
    'brother1': {
        'name': 'Jackson',
        'age': 23
    },
    'brother2': {
        'name': 'Hunter',
        'age': 28
    }
}

# family = set()

# for member, value in my_family.items():
#     family.add(f'{value["name"]} is my {member} and is {str(value["age"])} years old')
#     print(family)

family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}

print("My family!", family_stuff)




