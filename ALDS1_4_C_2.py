import sys

input = sys.stdin.readline
n = int(input())

dic = set()
for i in range(n):
  o, s = input().split()
  if o == 'insert':
    dic.add(s)
  else:
    if s in dic:
      print('yes')
    else:
      print('no')


  
