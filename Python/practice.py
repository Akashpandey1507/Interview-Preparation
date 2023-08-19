# Exercise 1A: Create a string made of the first, middle and last character

# take input form user
strings = input('Enter you strings: ')
# replace space with none
strings = strings.replace(' ','')
# apply changes
changes = strings[0::2]

# show
print(f'The String input from user is {strings} and the result is {changes}')