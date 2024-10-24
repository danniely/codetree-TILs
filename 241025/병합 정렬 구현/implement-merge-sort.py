n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))

def merge_arr(arr1: list, arr2: list) -> list:
    new_arr = []
    first_index = second_index = 0

    while first_index < len(arr1) and second_index < len(arr2):
        if arr1[first_index] < arr2[second_index]:
            new_arr.append(arr1[first_index])
            first_index += 1
        else:
            new_arr.append(arr2[second_index])
            second_index += 1

    if first_index == len(arr1):
        new_arr.extend(arr2[second_index : ])
    else:
        new_arr.extend(arr1[first_index : ])
    
    return new_arr


def merge_sort(arr):
    # basecase
    if len(arr) == 2:
        return [min(arr), max(arr)]
    
    if len(arr) == 1:
        return [arr[0]]
    
    if len(arr) == 0:
        return []

    L = 0
    R = len(arr)-1

    mid = (L + R)//2

    left_arr = merge_sort(arr[L:mid])
    right_arr = merge_sort(arr[mid:R+1])

    return merge_arr(left_arr, right_arr)


sorted_arr = merge_sort(arr)
for elem in sorted_arr:
    print(elem, end=" ")