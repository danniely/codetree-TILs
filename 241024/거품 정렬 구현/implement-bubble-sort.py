n = input()
arr = list(map(int, input().split(" ")))

def bubble_sort(arr):    
    n = len(arr)
    while is_sorted == False:
        is_sorted = True

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
    
    return arr

ans = " ".join(arr)
print(ans)