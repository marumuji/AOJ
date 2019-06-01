n = int(input())

dic = []
for i in range(n):
  o, s = input().split()
  if o == 'insert':
    dic.append(s)
  else:
    if s in dic:
      print('yes')
    else:
      print('no')



  
