from collections import deque
import copy
import itertools
import sys

sys.stdin = open("input.txt", "r")


def get_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return (x2-x1)**2 + (y2-y1)**2


def get_santas_list(santas_map):
    return list(santas.items())

def get_closest_santa_index(rud_x, rud_y, santas_map):
    min_dist = 9999999
    closest_santa_index = -1
    for santa in get_santas_list:
        d = get_dist((rud_x, rud_y), (santa['x'], santa['y']))
        if d < min_dist:
            min_dist = d
            closest_santa_index = santa['index']
    
    return closest_santa_index


def handle_pushback_santa():
    return 1


def move_rudolph_to_santa(grid, rud_x, rud_y, santas_map, rudolph_power):
    closest_santa_index = get_closest_santa_index(rud_x, rud_y, santas_map)
    closest_santa = santas_map.get(closest_santa_index)
    
    santa_x = closest_santa['x']
    santa_y = closest_santa['y']
    
    dx = santa_x - rud_x
    dy = santa_y - rud_y

    grid[rud_y][rud_x] = 0

    if abs(dx) > abs(dy):
        dist_x = 1 if rud_x < santa_x else -1
        rud_x += dist_x
    elif abs(dx) < abs(dy):
        dist_y = 1 if rud_y < santa_y else -1 
        rud_y += dist_y
    elif abs(dx) == abs(dy):
        # 대각선으로 이동
        dist_x = 1 if rud_x < santa_x else -1
        dist_y = 1 if rud_y < santa_y else -1
        rud_x += dist_x
        rud_y += dist_y

    # 루돌프 -> 산타 충돌할시, 루돌프힘만큼 점수 부여
    if (rud_x, rud_y) == (santa_x, santa_y):
        santas_map[closest_santa_index].score += rudolph_power
        santa_pushback_x = dist_x * c
        santa_pushback_y = dist_y * c

        handle_pushback_santa()

    else:
        grid[rud_y][rud_x] = -1


def solve(N, turns, num_santas, rudolph_power, santa_power, rudolph_x, rudolph_y):
    # for turn in range(turns):
    return 1


def main():
    N, turns, num_santas, rudolph_power, santa_power = list(map(int, input().strip().split(" ")))
    rudolph_y, rudolph_x = list(map(int, input().strip().split(" ")))

    rudolph_y -= 1
    rudolph_x -= 1
    
    santas_map = dict()

    for _ in range(num_santas):
        santa_index, santa_y, santa_x = list(map(int, input().strip().split(" ")))
        santas_map[santa_index] = {
            "x": santa_x - 1,
            "y": santa_y - 1,
        }
    
    # santas_map = sorted(santas_map, key = lambda x: (x["index"]))

    print(santas_map)

    grid = [[0 for _ in range(N)] for _ in range(N)]
        

    # rudolph = -1
    # santa = santa_index

    grid[rudolph_y][rudolph_x] = -1
    for santa in santas_map.items():
        santa_index, santa_pos = santa

        grid[santa_pos["y"]][santa_pos["x"]] = santa_index

    print(grid)
    # result = solve(N, turns, num_santas, rudolph_power, santa_power, rudolph_x, rudolph_y)
    # print(result)

main()