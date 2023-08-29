lists = []

for i in range(10):
    ask_num = int(input('Enter the Number: '))
    lists.append(ask_num)

print(f"The Sum of list is: {sum(lists)}")

multiply = 1

for i in lists:
    multiply = multiply * i

print(f'the Multiply is: {multiply}')

print(f"The min values is {min(sorted(lists))}.")
print(f"The max values is {max(sorted(lists))}.")