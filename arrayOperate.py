# array traverse
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title(),',that was a great trick!')
    print("I can't wait to see your next trick, "+magician.title() + ".\n")

# range()
for value in range(1,6):
    print(value)
# list() range()
numbers = list(range(1,6))
print(numbers)
even_number = list(range(2,11,2))
print(even_number)
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# number statistics
digits = [1,2,3,4,5,6,7,8,9,0]
min = min(digits)
print(min)
max = max(digits)
print(max)
sum = sum(digits)
print(sum)

# array analyse
squares = [value**2 for value in range(11,21)]
print(squares)
cubes = [value**3 for value in range(1,11)]
print(cubes)

# slice
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
    print(player.title())
# copy array
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)
# error copy methods
new_foods = ['pizza','falafel','carrot cake']
another_foods = new_foods
new_foods.append('cannoli')
another_foods.append('ice cream')
print(new_foods)
print(another_foods)

# tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
for dimension in dimensions:
    print(dimension)
