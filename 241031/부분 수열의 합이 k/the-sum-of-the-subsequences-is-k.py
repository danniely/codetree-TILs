n, k = list(map(int, input().strip().split(" ")))
arr = list(map(int, input().strip().split(" ")))

# brute-force: use 2 nested for-loop => O(n^2)

# prefix = [1 3 4 6]
# sliding_window -> L, R = 0, 0
# if prefix[R]-prefix[L-1] == k -> append to answer
# if prefix[R]-prefix[L-1] > target -> shift L += 1
# if prefix[R]-prefix[L] < k -> R -= 1
# while L <= R


def sumOfSubarraysEqualK(arr, n, k):
    prefix_sum = [0]*(n+1)

    # compute prefix sum
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    
    # print("prefix_sum: ", prefix_sum)
    L, R = 1,1
    ans = 0
    while L <= R and R < n+1:
        if prefix_sum[R] - prefix_sum[L-1] == k:
            ans += 1
            L += 1
            R += 1
        elif prefix_sum[R] - prefix_sum[L-1] > k:
            L += 1
        else:
            R += 1
    
    return ans

print(sumOfSubarraysEqualK(arr, n, k))