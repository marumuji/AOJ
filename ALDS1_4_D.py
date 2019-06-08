def searchMaxCapacity(w, k, p):
  unit_total = 0
  unit_num = 1

  for i in w:
    if i <= p:
      unit_total += i
      if unit_total > p:
        unit_num += 1
        if unit_num > k:
          return False
        unit_total = i
    else:
      return False
  return True
        
      
n, k = input().split()
n = int(n)
k = int(k)

w = [None] * n
for i in range(n):
  weit = int(input())
  w[i] = weit

left = 0
ans = right = 100000 * 10000

'''
using binary search argorithm
refer to below link

http://judge.u-aizu.ac.jp/onlinejudge/commentary.jsp?id=ALDS1_4_B&pattern=post&type=general&filter=Algorithm
'''
while left <= right:
  mid = (left + right) // 2
  if searchMaxCapacity(w, k, mid):
    ans = mid
    right = mid - 1
  else:
    left = mid + 1

print(ans)



