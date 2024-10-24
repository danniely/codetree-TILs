n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))

def selection_sort(arr):
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    

selection_sort(arr)

for elem in arr:
    print(elem, end=" ")