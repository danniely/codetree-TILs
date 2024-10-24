n = input()
arr = list(map(int, input().split(" ")))

def bubble_sort(arr):    
    n = len(arr)
    is_sorted = False
    while is_sorted == False:
        is_sorted = True

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
    
    return arr

bubble_sort(arr)

for elem in arr:
    print(elem, end=" ")