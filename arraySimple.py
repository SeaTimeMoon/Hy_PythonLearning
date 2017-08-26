# what's array
bikes = ['trek','cannondale','redline','specialized']
print(bikes)
print(bikes[0].title())
print(bikes[1].title())
print(bikes[2].title())
print(bikes[3].title())

print(bikes[-1].title())

message = "My first bike is a " + bikes[0].title() + "."
print(message)

# modify/add/delete array element
# modify
motobikes = ['honda','yamaha','suzuki']
print(motobikes)
motobikes[0] = 'ducati'
print(motobikes)
# add
motobikes.append('ducati')
print(motobikes)
#insert
motobikes.insert(0,'newmoto')
print(motobikes)
#delete
del motobikes[0]
print(motobikes)
del motobikes[1]
print(motobikes)
#pop
motobikes.pop()
print(motobikes)
popbike = motobikes.pop()
print(popbike)
motobikes = ['honda','yamaha','suzuki']
firstOwned = motobikes.pop(0)
print('The first motobike I owned was a ' + firstOwned.title() + '.')
#remove
motobikes.remove('yamaha')
print(motobikes)

# organize array
# sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\n Here is the sorted list:")
print(sorted(cars))
print("\n Here is the original list again:")
print(cars)
# reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#len
length = len(cars)
print(str(length))