# file read
# simple example
path = 'pi_digits.txt'
with open(path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(path) as file_object2:
    for line in file_object2:
        print(line.rstrip())
#list
with open(path) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# big data process
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object4:
#     new_lines = file_object4.readlines()
#
# pi_string_long = ''
# for line in new_lines:
#     pi_string_long += line.strip()
#
# print(pi_string_long[:128] + '...')
# print(len(pi_string_long))

# pi contains your birthday
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string_long:
#     print("Your birthday appears in the first million digits of pi")
# else:
#     print("Your birthday does not appear in the first million digits of pi")



# file write

# write an empty file
filename = 'programming1.txt'
with open(filename, 'w') as file_object5:
    file_object5.write("I love programming.")

# write multi line
filename = 'programming2.txt'
with open(filename, 'w') as file_object6:
    file_object6.write("I love programming.\n")
    file_object6.write("I love creating new games.\n")

# add additional message in files
filename2 = 'programming2.txt'
with open(filename2, 'a') as file_object7:
    file_object7.write("I also love finding meaning in large datasets.\n")
    file_object7.write("I love creating apps that can run in a browser.\n")


#Exception

#ZeroDivisionError
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)


# FileNotFoundError

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg+'\n')


# Words Analyse

def count_words(file_name_path):
    """calculate the words count in a file"""
    try:
        with open(file_name_path) as f_obj10:
            contents = f_obj10.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filenamepath + " does not exist."
        # print(msg)
        pass
    else:
        # calculate words count in file
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name_path + " has about " + str(num_words) + " words.")

file_names = ['A Creature of the Night.txt','Alice in wonderland','David Copperfield.txt','Jane Eyre.txt','Aesop’s Fables.txt'
              ,'a tale of two cities.txt']
for filename in file_names:
    count_words(filename)


