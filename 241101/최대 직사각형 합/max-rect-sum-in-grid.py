n = int(input().strip())
grid = []
grid = [list(map(int, input().strip().split(" "))) for _ in range(n)]

prefix_sum = [[0] * (n+1) for _ in range(n+1)]

for y in range(n):
    for x in range(n):
        prefix_sum[y+1][x+1] = prefix_sum[y+1][x] + prefix_sum[y][x+1] - prefix_sum[y][x] + grid[y][x]

# [0, 0, 0, 0]
# [0, 1, 3, 6]
# [0, 7, -891, -881]
# [0, 14, -877, -858]

# print(*prefix_sum, sep="\n")
max_sum = 0
for y_i in range(1, n+1):
    for x_i in range(1, n+1):
        for y_j in range(y_i, n+1):
            for x_j in range(x_i, n+1):
                curr_sum = prefix_sum[y_j][x_j] - prefix_sum[y_j][x_i-1] - prefix_sum[y_i-1][x_j] + prefix_sum[y_i-1][x_i-1]
                max_sum = max(max_sum, curr_sum)

print(max_sum)