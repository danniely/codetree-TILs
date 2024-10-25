n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))

def choose_pivot(arr, low, high):
    if high - low + 1 <= 3:
        return high  # If 3 or fewer elements, choose the last element as the pivot

    else:
        first, mid, last = arr[low], arr[(low + high) // 2], arr[high]
        # Find the median of the three elements
        median = sorted([(first, low), (mid, (low + high) // 2), (last, high)], key = lambda x: x[0])[1]
        return median[1]  # Return the index of the median element


def partition(arr, low, high):
    pivot_index = choose_pivot(arr, low, high)
    pivot = arr[pivot_index]

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

quick_sort(arr, 0, n-1)

for elem in arr:
    print(elem, end=" ")