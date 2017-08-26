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

# while True:
#     print('\nPlease tell me your name:')
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# list parameters
def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

new_unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
new_completed_models = []
print_models(new_unprinted_designs[:], new_completed_models)
print(new_unprinted_designs)


# 任意数量的实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

# 任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeteon',field='physics')
print(user_profile)
