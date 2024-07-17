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
    return list(santas_map.items())


def get_closest_santa_index(rud_x, rud_y, santas_map):
    min_dist = 9999999
    closest_santa_index = -1

    ties = []
    for santa_index, santa in get_santas_list(santas_map):
        d = get_dist((rud_x, rud_y), (santa['x'], santa['y']))
        if d < min_dist:
            min_dist = d
            closest_santa_index = santa_index
        if d == min_dist:
            ties.append({
                "dist": d,
                "x": santa['x'],
                "y": santa['y'],
                "index": santa_index
            })
    
    ties = sorted(ties, key=lambda elem: (elem['dist'], -elem['y'], -elem['x']))

    return ties[0]['index']


def get_direction(dx, dy):
    # 가로
    if dy == 0:
        if dx < 0:
            return 6 # 좌
        else:
            return 2 # 우

    # 세로
    elif dx == 0:
        if dy < 0:
            return 0 # 상
        else:
            return 4 # 하
    
    # 대각선
    else:
        if dy < 0:
            if dx < 0:
                return 7 # 상좌
            else:
                return 1 # 상우
        else:
            if dx < 0:
                return 5 # 하좌
            else:
                return 3 # 하우



def handle_pushback_santa(N, grid, rud_dist_x, rud_dist_y, rud_power, santas_map, santa_index):
    santa_x = santas_map[santa_index]['x']
    santa_y = santas_map[santa_index]['y']

    print("santas_map[santa_index]: ", santas_map[santa_index])

    next_santa_x = santa_x + rud_dist_x
    next_santa_y = santa_y + rud_dist_y

    prev_santa_x = next_santa_x
    prev_santa_y = next_santa_y

    print(f"next_santa_x: {next_santa_x}")
    print(f"next_santa_y: {next_santa_y}")

    direction = get_direction(rud_dist_x, rud_dist_y)


    print("direction: ", direction)

    if (
            (santa_x == 0 and direction > 4) or
            (santa_x == N-1 and 0 < direction < 4) or
            (santa_y == 0 and direction < 3) or 
            (santa_y == 0 and direction > 6) or 
            (santa_y == N-1 and 3 < direction < 6)
        ):
            print("santa is kicked(1)")
            grid[santa_y][santa_x] = 0
            del santas_map[santa_index]

            return None
    
    if (next_santa_y < 0 or next_santa_y >= N or next_santa_x < 0 or next_santa_x >= N):
        print("santa is kicked(2)")
        grid[santa_y][santa_x] = 0
        del santas_map[santa_index]

        return None

    prev_santa = grid[santa_y][santa_x]
    next_santa = grid[next_santa_y][next_santa_x]

    while next_santa != 0 and 0 < next_santa_x < N and 0 < next_santa_y < N:

        grid[next_santa_y][next_santa_x] = prev_santa
        next_santa_index = grid[next_santa_y][next_santa_x]
        
        prev_santa_x = next_santa_x
        prev_santa_y = next_santa_y

        prev_santa = next_santa
        
        if direction == 0:
            next_santa_y -= 1
        
        elif direction == 1:
            next_santa_y -= 1
            next_santa_x += 1
        
        elif direction == 2:
            next_santa_x += 1
        
        elif direction == 3:
            next_santa_y += 1
            next_santa_x += 1
        
        elif direction == 4:
            next_santa_y += 1

        elif direction == 5:
            next_santa_y += 1
            next_santa_x -= 1

        elif direction == 6:
            next_santa_x -= 1
        
        elif direction == 7:
            next_santa_y -= 1
            next_santa_x -= 1
        
        santas_map[santa_index]['x'] = prev_santa_x
        santas_map[santa_index]['y'] = prev_santa_y
        santas_map[next_santa_index]['x'] = next_santa_x
        santas_map[next_santa_index]['y'] = next_santa_y


        print(f"santas_map[santa_index]: {santas_map[santa_index]}")
        print(f"santas_map[next_santa_index]: {santas_map[next_santa_index]}")

    grid[next_santa_y][next_santa_x] = prev_santa

    print(f"prev_santa_x: {prev_santa_x}, prev_santa_y:{prev_santa_y}")

    next_santa_index = grid[next_santa_y][next_santa_x]
    santas_map[santa_index]['x'] = prev_santa_x
    santas_map[santa_index]['y'] = prev_santa_y

    print("next_santa_index: ", next_santa_index)
    if next_santa_index >= 1:
        print(f"updating next_santa_index({next_santa_index}) from {santas_map[next_santa_index]} to {next_santa_x}, {next_santa_y}")
        santas_map[next_santa_index]['x'] = next_santa_x
        santas_map[next_santa_index]['y'] = next_santa_y

    grid[santa_y][santa_x] = 0


def move_rudolph_to_santa(N, grid, rud_x, rud_y, santas_map, rudolph_power):
    print("grid before move(rudolph)")
    print(*grid, sep="\n")

    closest_santa_index = get_closest_santa_index(rud_x, rud_y, santas_map)
    closest_santa = santas_map.get(closest_santa_index)
    
    santa_x = closest_santa['x']
    santa_y = closest_santa['y']

    print(f"closest_santa: {closest_santa}")
    
    dx = santa_x - rud_x
    dy = santa_y - rud_y

    print(f"dx:{dx}, dy:{dy}")

    grid[rud_y][rud_x] = 0

    dist_y = 0
    dist_x = 0

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
        print("collide!")
        santas_map[closest_santa_index]['knockout'] = 1
        santas_map[closest_santa_index]['score'] += rudolph_power
        santa_pushback_x = dist_x * rudolph_power
        santa_pushback_y = dist_y * rudolph_power

        handle_pushback_santa(N, grid, santa_pushback_x, santa_pushback_y, rudolph_power, santas_map, closest_santa_index)
        grid[rud_y][rud_x] = -1

    else:
        grid[rud_y][rud_x] = -1
    
    print("grid after move(rudolph)")
    print(*grid, sep="\n")

    return (rud_x, rud_y)


def move_santa_to_rudolph(N, grid, rud_x, rud_y, santas_map, santa_power):
    for santa_index, santa in list(santas_map.items()):
        print(f"grid before move(santa[{santa_index}])")
        print(*grid, sep="\n")
        print("santas_map: ", santas_map)

        santa_x, santa_y = santa['x'], santa['y']
        dx = santa_x - rud_x
        dy = santa_y - rud_y

        if (santas_map[santa_index]['knockout']) % 2 is not 0:
            print(f"{santa_index} santa is knockedout. ")
            santas_map[santa_index]['knockout'] = (santas_map[santa_index]['knockout'] + 1) % 2
            continue

        # print(f"dx:{dx}, dy:{dy}")

        # grid[santa_y][santa_x] = 0

        dist_y = 0
        dist_x = 0

        new_santa_x = santa_x
        new_santa_y = santa_y

        if rud_x > santa_x:
            dist_x = 1
        elif rud_x < santa_x:
            dist_x = -1
        else:
            dist_x = 0
        
        if rud_y > santa_y:
            dist_y = 1
        elif rud_y < santa_y:
            dist_y = -1
        else:
            dist_y = 0

        new_santa_x += dist_x
        new_santa_y += dist_y

        # if abs(dx) > abs(dy):
        #     dist_x = 1 if rud_x > santa_x else -1
        #     new_santa_x += dist_x
        # elif abs(dx) < abs(dy):
        #     dist_y = 1 if rud_y > santa_y else -1 
        #     new_santa_y += dist_y
        
        # elif abs(dx) == abs(dy):
        #     # 대각선으로 이동은 못하지만 상하좌우로 선택해서 움직일수는 있음.
        #     dist_x = 1 if rud_x > santa_x else -1
        #     dist_y = 1 if rud_y > santa_y else -1

        if grid[new_santa_y][santa_x] >= 1 and grid[santa_y][new_santa_x] >= 1:
            print("cannot move!")
            # 다 막혀있는 상태
            continue
        
        # 상우하좌 순서로 움직임.
        if dist_y == -1 and grid[new_santa_y][santa_x] == 0:
            # 상
            new_santa_x = santa_x

        elif dist_x == 1 and grid[santa_y][new_santa_x] == 0:
            # grid[santa_y][new_santa_x] = santa_index
            new_santa_y = santa_y

        elif dist_y == 1 and grid[new_santa_y][santa_x] == 0:
            # grid[new_santa_y][santa_x] = santa_index
            new_santa_x = santa_x

        elif dist_x == -1 and grid[santa_y][new_santa_x] == 0:
            # grid[santa_y][new_santa_x] = santa_index
            new_santa_y = santa_y
            
        # 산타 충돌할시, 산타 힘만큼 점수 부여
        if (rud_x, rud_y) == (new_santa_x, new_santa_y):
            print("collide!")
            # grid[santa_y][santa_x] = 0
            santas_map[santa_index]['knockout'] = 1
            santas_map[santa_index]['score'] += santa_power
            santa_pushback_x = dist_x * santa_power
            santa_pushback_y = dist_y * santa_power

            handle_pushback_santa(N, grid, -santa_pushback_x, -santa_pushback_y, santa_power, santas_map, santa_index)
        
            print("grid after collision(santa)")
            print(*grid, sep="\n")
            continue

        if (new_santa_x, new_santa_y) != (santa_x, santa_y):
            # 이전과 위치가 다르다면, 움직였다는 뜻.
            if grid[new_santa_y][new_santa_x] >= 1:
                print("something blocked!!")
                continue
            print("moved!")
            grid[santa_y][santa_x] = 0
            grid[new_santa_y][new_santa_x] = santa_index
            santas_map[santa_index] = {
                "x": new_santa_x,
                "y": new_santa_y,
                "score": santa['score'],
                "knockout": santa['knockout'],
            }
            continue
    # return (rud_x, rud_y)

def solve(N, grid, santas_map, turns, num_santas, rudolph_power, santa_power, rudolph_x, rudolph_y):
    for turn in range(turns):
        rudolph_x, rudolph_y = move_rudolph_to_santa(N, grid, rudolph_x, rudolph_y, santas_map, rudolph_power)
        move_santa_to_rudolph(N, grid, rudolph_x, rudolph_y, santas_map, santa_power)
    return 1


def main():
    N, turns, num_santas, rudolph_power, santa_power = list(map(int, input().strip().split(" ")))
    rudolph_y, rudolph_x = list(map(int, input().strip().split(" ")))

    rudolph_y -= 1
    rudolph_x -= 1

    print(f"rudolph_y: {rudolph_y}")
    print(f"rudolph_x: {rudolph_x}")
    
    santas_map = dict()

    for _ in range(num_santas):
        santa_index, santa_y, santa_x = list(map(int, input().strip().split(" ")))
        santas_map[santa_index] = {
            "x": santa_x - 1,
            "y": santa_y - 1,
            "score": 0,
            "knockout": 0,
        }
    
    # santas_map = sorted(santas_map, key = lambda x: (x["index"]))

    # print(santas_map)

    grid = [[0 for _ in range(N)] for _ in range(N)]
        

    # rudolph = -1
    # santa = santa_index

    grid[rudolph_y][rudolph_x] = -1
    for santa in santas_map.items():
        santa_index, santa_pos = santa

        grid[santa_pos["y"]][santa_pos["x"]] = santa_index

    # print(grid)
    result = solve(N, grid, santas_map, turns, num_santas, rudolph_power, santa_power, rudolph_x, rudolph_y)
    # print(result)

main()