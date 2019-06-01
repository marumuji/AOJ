import re

def porland(input_array):
  stack = []
  num = '\d'
  for i in input_array:
    if re.match(num, i):
      stack.append(int(i))
    else:
      second = stack.pop(-1)
      first = stack.pop(-1)
      if i == '+':
        stack.append(first + second)
      if i == '-':
        stack.append(first - second)
      if i == '*':
        stack.append(first * second)
  return stack
    
input_array = input("").split()
print(porland(input_array).pop(0))
