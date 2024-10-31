n, k = list(map(int, input().strip().split(" ")))
grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]

# brute-force = O((n-k)(n-k)(k*k)) = O(n^2 * k^2)
def getSum(grid: list[list]) -> int:
    # print(*grid, sep="\n")
    prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # computing prefix_sum
    for y in range(1, n+1):
        for x in range(1,n+1):
            prefix_sum[y][x] = prefix_sum[y][x-1] + prefix_sum[y-1][x] - prefix_sum[y-1][x-1] + grid[y-1][x-1]

    sum_max = 0
    for y in range(k, n+1):
        for x in range(k,n+1):
            curr_max = prefix_sum[y][x] - prefix_sum[y-k][x] - prefix_sum[y][x-k] + prefix_sum[y-k][x-k]
            sum_max = max(sum_max, curr_max)
    
    return sum_max

    # [1    3   6]
    # [10   20  31]
    # [16   34  53]

print(getSum(grid))

# 53-16-6+1 = 53-22+1 = 32