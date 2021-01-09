import sys

N = int(sys.stdin.readline())
# min_total = 293248438394
max_total = 0
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# pair : (0, 5), (1, 3), (2, 4)
pair = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

for i in range(6):
    temp = 0
    k = 0
    n = matrix[0][i]
    while k < N:
        idx = matrix[k].index(n)
        bottom = matrix[k][idx]
        top = matrix[k][pair[idx]]
        mV = 6
        while mV > 1:
            if mV == bottom or mV == top:
                mV -= 1
            else:
                break
        temp += mV
        n = top
        k += 1
    if temp > max_total:
        max_total = temp


print(max_total)
