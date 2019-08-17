def solve(i, m):
  if m == 0:
    return True
  if i >= n:
    return False

  res = solve(i + 1, m) or solve(i + 1, m - a[i])
  return res


n = int(input())
a = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]

for i in m:
  if sum(a) < i:
    print("no")    
  elif solve(0, i):
    print("yes")
  else:
    print("no")

