def linearSearch(s, key):
  i = 0
  s.append(key) 
  while s[i] != key:
    i += 1
    if i == len(s)-1:
      return 0
  return 1
   

n = int(input())
s = input().split()
q = int(input())
t = input().split()

count = 0
for i in t:
  count += linearSearch(s, i)
print(count)

