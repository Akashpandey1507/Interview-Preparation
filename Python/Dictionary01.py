# Write a Python script to check whether a given key already exists in a dictionary.

number = int(input('Enter the number to check: '))

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}  

if number in d:
    print('Yes, the Key is already exists.')
else:
    print('No, the Key is not exists.')