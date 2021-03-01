def trip(k, w, v):
    global maxV
    if w > K :
        return
    if v > maxV :
        maxV = v
    if k >= N :
        return
    visit[k] = 1
    trip(k+1, w + info[k][0], v + info[k][1])
    visit[k] = 0
    trip(k + 1, w, v)

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
# W (무게), V(가치)
maxV = 0
visit = [0] * N
trip(0, 0, 0)

print(maxV)