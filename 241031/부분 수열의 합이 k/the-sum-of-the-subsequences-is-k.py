n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))

prefix_sum = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

ans = -100 * 100000 * 100000

# prefix cannot have the same number (the minimum value of given numbers is 1)

nums = set(prefix_sum)
ans = 0 

for num in nums:
    if (num - k) in nums:
        ans += 1
    
print(ans)