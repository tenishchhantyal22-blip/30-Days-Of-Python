# Exercise day 8 (Dictionaries)
empty_dog = {}
empty_dog = {
    'name': 'Tenesh',
    'color': 'Red',
    'breed': 'Human',
    'legs': 'Right',
    'Age': 19
}
student_dictionary = {
    'first_name': 'Toni',
    'last_name': 'Stark',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'unmarried',
    'skills': ['Python', 'Java', 'AI', 'ML'],
    'Country': 'Nepal',
    'City': 'Pokhara',
    'Address': {
        'home': 'Beni',
        'postal_code':'230A'
    }
}
print(len(student_dictionary))
print(student_dictionary['skills'])

student_dictionary['skills'].append('Coding')
print(student_dictionary)

keys = student_dictionary.keys
print(student_dictionary)

values = student_dictionary.values
print(student_dictionary)

print(student_dictionary.items())

del student_dictionary['age']
print(student_dictionary)

student_dictionary.clear()
print(student_dictionary)
