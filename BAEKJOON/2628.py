import sys

def get_res(lst, maxl, rlst):
    s = 0
    if lst:
        for i in range(len(lst)):
            rlst.append(lst[i]-s)
            s = lst[i]
            if i == len(lst) -1:
                rlst.append(maxl - s)
    else:
        rlst.append(maxl)



width, height = map(int, sys.stdin.readline().split())
N = int(input())
w =[]
h = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0:
        w.append(b)
    else:
        h.append(b)
# cut = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
w.sort()
h.sort()

garo = []
sero = []


get_res(h, width, garo)
get_res(w, height, sero)

total = 0
for i in range(len(garo)):
    for j in range(len(sero)):
        if garo[i] * sero[j] >= total:
            total = garo[i] * sero[j]
print(total)