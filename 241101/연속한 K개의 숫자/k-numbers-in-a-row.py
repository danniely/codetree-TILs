n, k, b = list(map(int, input().strip().split(" ")))

excludes = []
for i in range(b):
    excludes.append(int(input().strip()))

arr = [0]*(n+1)
prefix_sum = [0]*(n+1)

for exclude in excludes:
    arr[exclude] = 1

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

min_num = n

for i in range(k, n+1):
    L = i-k
    R = i
    min_num = min(min_num, prefix_sum[R]-prefix_sum[L])

print(min_num)