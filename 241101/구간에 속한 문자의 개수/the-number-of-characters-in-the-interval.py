n,m,k = list(map(int, input().strip().split(" ")))

grid = [[0]*m for _ in range(n)]
prefix_sum = [[(0,0,0)]*(m+1) for _ in range(n+1)]

for y in range(n):
    row = input().strip()
    for x, elem in enumerate(row):
        if elem == 'a':
            grid[y][x] = (1,0,0)
        elif elem == 'b':
            grid[y][x] = (0,1,0)
        elif elem == 'c':
            grid[y][x] = (0,0,1)

def add_tuple(p1, p2):
    return tuple(map(lambda i,j: i+j, p1, p2))

def minus_tuple(p1, p2):
    return tuple(map(lambda i,j: i-j, p1, p2))


for y in range(n):
    for x in range(m):
        add1 = add_tuple(prefix_sum[y][x+1], prefix_sum[y+1][x])
        minus1 = minus_tuple(add1, prefix_sum[y][x])
        add2 = add_tuple(minus1, grid[y][x])
        prefix_sum[y+1][x+1] = add2

for _ in range(k):
    r1,c1,r2,c2 = list(map(int, input().strip().split(" ")))
    result1 = minus_tuple(prefix_sum[r2][c2], prefix_sum[r2][c1-1])
    result2 = minus_tuple(result1, prefix_sum[r1-1][c2])
    result3 = add_tuple(result2, prefix_sum[r1-1][c1-1])

    for elem in result3:
        print(elem, end=" ")
    print()