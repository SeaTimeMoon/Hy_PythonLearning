# input example

# name = input('Please enter your name: ')
# print("Hello " + name + '!')

# prompt = 'If you tell us who you are, we can personalize the messages you see'
# prompt += '\nWhat is your first name? '
# name = input(prompt)
# print('\nHello, ' + name + '!')

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print('\nThe number ' + str(number) + ' is even.')
# else:
#     print('\nThe number ' + str(number) + ' is odd.')

# prompt = '\nTell me something, and I will repeat it back to you: '
# prompt += "\n Enter 'quit' to end the program. "
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = '\n Please enter the name of a city you have visited: '
# prompt += "\n(Enter 'quit' when you are finished) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + '!')

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# use 'while' to handle list and dictionary
# move list element
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# delete all special list element
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# input several messages with 'while'
responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')