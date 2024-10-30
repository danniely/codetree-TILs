from functools import reduce

n, k = list(map(int, input().strip().split(" ")))
arr = list(map(int, input().strip().split(" ")))

# arr: -10 10 -4 4 1
# prefix: -10 0 -4 0 1

def max_sum_k_consecutive(arr, k):
    # prefix_sum = [0] + reduce(lambda acc, x: acc + [acc[-1]+x], arr[1:], [arr[0]])
    # prefix_sum = [0]
    # for elem in arr:
    #     prefix_sum.append(prefix_sum[-1]+elem)
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    max_sum = -float('inf')
    for i in range(k-1,len(prefix_sum)):
        current_range_sum = prefix_sum[i]-prefix_sum[i-k]
        max_sum = max(max_sum, current_range_sum)

    return max_sum


print(max_sum_k_consecutive(arr, k))