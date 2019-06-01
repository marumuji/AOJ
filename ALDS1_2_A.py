def bubbleSort(i_array):
  flag = 1
  count = 0
  i = 0
  while flag:
    flag = 0
    for j in range(len(i_array) - 1, i, -1):
      if i_array[j] < i_array[j-1]:
        i_array[j], i_array[j-1] = i_array[j-1], i_array[j]
        count += 1
        flag = 1
    i += 1
  return i_array, count
  
  
length = input("")
c_array = input("").split()
i_array = [int(i) for i in c_array]

sorted_array, times = bubbleSort(i_array)
print(*sorted_array)
print(times)
