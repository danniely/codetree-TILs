from collections import deque
import copy
import itertools
import sys

# sys.stdin = open("input.txt", "r")

n = 5

def obtain_prize(grid):
    def bfs(_x, _y):
        queue = deque([(_x, _y)])
        same_block_queue = deque([(_x, _y)])
        visited.add((_x, _y))

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_y][new_x] == grid[_y][_x]:
                    visited.add((new_x, new_y))
                    same_block_queue.append((new_x, new_y))
                    queue.append((new_x, new_y))
        return same_block_queue

    total_prize = 0
    n = len(grid)
    visited = set()

    for y in range(n):
        for x in range(n):
            if (x, y) not in visited and grid[y][x] != -1:
                block = bfs(x, y)
                if len(block) >= 3:
                    total_prize += len(block)
                    while block:
                        pop_x, pop_y = block.popleft()
                        grid[pop_y][pop_x] = -1
    return total_prize

def refill_prizes(grid, new_prizes):
    for x in range(n):
        for y in range(n-1, -1, -1):
            if grid[y][x] == -1:
                if len(new_prizes) > 0:
                    pop_value = new_prizes.popleft()
                    grid[y][x] = pop_value

def deep_copy(grid):
    return copy.deepcopy(grid)

def print_grid(grid):
    for row in grid:
        row_str = list(map(str, row))
        print(" ".join(row_str))
    print("\n")

def rotate_grid(grid, degree, x, y):
    # Extract the 3x3 subgrid
    grid_copy = deep_copy(grid)
    subgrid = [row[x-1:x+2] for row in grid_copy[y-1:y+2]]
    
    # Rotate the subgrid based on the degree
    if degree == 1:
        subgrid = rotate_90(subgrid)
    elif degree == 2:
        subgrid = rotate_180(subgrid)
    elif degree == 3:
        subgrid = rotate_270(subgrid)
    
    # Place the rotated subgrid back into the grid
    for i in range(3):
        for j in range(3):
            grid_copy[y-1+i][x-1+j] = subgrid[i][j]
    
    return grid_copy


def rotate_grid_and_get_prize(grid, degree, x, y):
    rotate_grid(grid, degree, x, y)
    local_prize = obtain_prize(grid)
    return local_prize, grid_copy

def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def rotate_270(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def find_the_best_option(candidates):
    # Sort by prize in descending order, degree in ascending order, x in ascending order, and y in ascending order
    candidates = sorted(candidates, key=lambda x: (-x['prize'], x['degree'], x['x'], x['y']))
    return candidates[0]

def run(grid_param, num_simulations, new_prizes: deque):
    grid = deep_copy(grid_param)
    prizes = []
    for each_simulation in range(num_simulations):
        total_prize = 0
        index_candidates = list(itertools.product(range(1, 4), repeat=2))
        max_candidates = []

        for coordinate in index_candidates:
            x, y = coordinate[0], coordinate[1]
            for degree in [1, 2, 3]:
                rotated_grid = rotate_grid(grid, degree, x, y)
                prize_from_rotated_grid = obtain_prize(rotated_grid)

                max_candidates.append({
                    "prize": prize_from_rotated_grid,
                    "degree": degree,
                    "x": x,
                    "y": y,
                    "grid": rotated_grid,
                })

        best_option = find_the_best_option(max_candidates)
        best_grid = best_option['grid']
        current_prize = best_option['prize']

        if current_prize == 0:
            continue

        grid = best_grid
        
        total_prize += current_prize

        # print("total_prize(first): ", total_prize)

        # print("new_prizes: ", new_prizes)

        # print("before refill")
        # print_grid(best_grid)
        
        refill_prizes(grid, new_prizes)

        # print("after refill")
        # print_grid(best_grid)

        new_prize = obtain_prize(grid)
 
        # print("after scavange")
        # print_grid(best_grid)

        while new_prize > 0 and len(new_prizes) >0:
            total_prize += new_prize
            refill_prizes(grid, new_prizes)

            # print("after refill")
            # print_grid(best_grid)

            new_prize = obtain_prize(grid)

            # print("after scavange")
            # print_grid(best_grid)       
        
        # print("total_prize(after): ", total_prize)
        prizes.append(total_prize)

    return prizes

def main():
    num_simulations, num_new_prizes = list(map(int, input().strip().split(" ")))
    _grid = []
    for _ in range(n):
        _grid.append(list(map(int, input().strip().split(" "))))
    
    new_prizez = deque(list(map(int, input().strip().split(" "))))
    result = run(_grid, num_simulations, new_prizez)
    str_result = " ".join(list(map(str, result)))
    print(str_result)

main()