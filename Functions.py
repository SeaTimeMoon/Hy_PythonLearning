#define functions
def greet_user(username):
     print("Hello, " + username.title() + "!")

greet_user('jesse')

def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet('dog','willie')

# key-value parameter
describe_pet(animal_type='cat',pet_name='gaffey')
describe_pet(pet_name='gaffey',animal_type='cat')

# default parameter value
def describe_pet2(pet_name, animal_type = 'dog'):
    print('I have a ' + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name='willie')


# return value
# simple return value
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
# optional actual parameter
def get_formatted_name2(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician2 = get_formatted_name2('jimi','hendrix')
print(musician2)

musician2 = get_formatted_name2('jimi','hendrix','lee')
print(musician2)

# return dictionary
def build_person(first_name, last_name, age = ''):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#
