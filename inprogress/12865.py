def trip(k, w, v):
    global minW, maxV
    if w >= gap
    visit[k] = 1
    trip(k+1, w + info[k][0], v + info[k][1])
    visit[k] = 0
    trip(k + 1, w, v)

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
# W (무게), V(가치)

totalW = 0
maxV = 0
for i in info:
    totalW += i[0]
    maxV += i[1]
minW = totalW
gap = totalW - K
visit = [0] * N
trip(0, 0, 0)

print(maxV)