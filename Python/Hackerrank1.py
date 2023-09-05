'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''


def is_weird(n):
  if n % 2 == 1:
    return "Weird"
  elif n >= 2 and n <= 5:
    return "Not Weird"
  elif n >= 6 and n <= 20:
    return "Weird"
  else:
    return "Not Weird"



n = int(input("Enter a number: "))
print(is_weird(n))



