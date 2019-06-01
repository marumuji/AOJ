val_1 = input('')
val_2 = input('').split()

def insertionSort(a, n):
    print(*a)
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j-=1
        a[j+1] = v
        print(*a)

int_length = int(val_1)
int_array = [int(i) for i in val_2 if i]
insertionSort(int_array, int_length)
