def binarySearch(s, i):
  left = 0
  right = len(s) 
  while left < right:
    mid = int((left + right) / 2)
    if s[mid] == i:
      return 1
    elif i < s[mid]:
      right = mid
    else:
      left = mid + 1
  return 0
   

n = int(input())
s = input().split()
s = [ int(i) for i in s]
q = int(input())
t = input().split()
t = [ int(i) for i in t]

count = 0
for i in t:
  count += binarySearch(s, i)
print(count)

