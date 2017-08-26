# simple example
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# condition test

# if sentence
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

# if else sentence
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote')
    print('Please register to vote as soon as you turn 18!')

# if-elif-else
age = 75
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age <65:
    price = 10
else:
    price = 5

print('Your admission cost is $' + str(price) + '.')

requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza')

# if sentence handle array
requested_toppings = ['mushrooms','green peppers','extra cheese']
for request_topping in requested_toppings:
    if request_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + request_topping + '.')

print('\nFinished making your pizza')

# array is empty
request_topping = []
if request_topping:
    for request_topping in requested_toppings:
        print('Adding ' + request_topping + '.')
    print('\nFinished making your pizza')
else:
    print('Are you sure you want a plain pizza?')

# multi array
available_toppings = ['mushrooms','olives','green pepper','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for request_topping in requested_toppings:
    if request_topping in available_toppings:
        print('Adding ' + request_topping + '.')
    else:
        print("Sorry, we don't have " + request_topping + ".")