# dictionary create, read
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print('You just earned ' + str(new_points) +' points!')
#dictionary add key and value
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
#dictionary create, add key and values, modify
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
alien_1['color'] = 'yellow'
print(alien_1)
#modify example
alien_2 = {'x_pos':0,'y_pos':25,'speed':'medium'}
print('Original x-pos :' + str(alien_2['x_pos']))

if alien_2['speed'] == 'slow':
    x_incremnt = 1
elif alien_2['speed'] == 'medium':
    x_incremnt = 2
else:
    x_incremnt = 3

alien_2['x_pos'] = alien_2['x_pos'] + x_incremnt
print('New x-pos: ' + str(alien_2['x_pos']))

#delete key-value
alien_3 = {'color':'green','points':5}
print(alien_3)
del alien_3['points']
print(alien_3)

#complex dictionary
favorite_languages  = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# traverse dictionary
#traverse items
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key,value in user_0.items():
    print('\nKey: ',key)
    print('value: ',value)

#traverse keys
favorite_languages  = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(' Hi ' + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# sorted traverse keys
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

# traverse values
print('The following languages have been mentioned: ')
for language in favorite_languages.values():
    print(language.title())

print('Only the following languages have been mentioned: ')
for language in set(favorite_languages.values()):
    print(language.title())

# dictionary list

# create a alien list
aliens = []
# create 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# display the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# display the created alien count
print('The total number of aliens: ' + str(len(aliens)))

# List Dictionary
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print('You ordered a ' + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil':['python','haskell'],
}
for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# dictionary dictionary
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())