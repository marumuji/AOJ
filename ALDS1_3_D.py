data=input()
stack = []
pond = []
total = 0
for i in range(len(data)):
  if data[i] == '\\':
    stack.append(i)
  elif stack and data[i] == '/':
    j = stack.pop()
    a = i - j
    total += a

    while pond and pond[-1][0] > j: 
      a += pond.pop()[1]
      
    pond.append([j, a])

print(total)
print(len(pond), *(a for j, a in pond))
    
    
