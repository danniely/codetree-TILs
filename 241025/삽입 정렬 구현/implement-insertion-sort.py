n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))

def insertion_sort(arr):
    for i in range(1, n):
        elem = arr[i]
        j = i-1
        while j >= 0 and arr[j] > elem:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = elem

insertion_sort(arr)

for elem in arr:
    print(elem, end=' ')