n, q = list(map(int, input().strip().split(" ")))
locations = list(map(int, input().strip().split(" ")))

max_location = max(locations)
# number of dots
array = [0]*((10**6)+1)
number_of_dots = [0]*((10**6)+1)

# array = [0 0 1 1 0 1 0 1]
for location in locations:
    array[location] = 1

# number_of_dots = [0 0 1 2 2 3 3 4]
for i in range(1, (10**6)+1):
    number_of_dots[i] = number_of_dots[i-1] + array[i]

for query in range(q):
    L, R = list(map(int, input().strip().split(" ")))
    if L >= 1:
        print(number_of_dots[R] - number_of_dots[L-1])
    else:
        print(number_of_dots[R])