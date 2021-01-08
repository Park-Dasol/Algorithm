import sys


def queen(k):
    global cnt
    if k == N:
        cnt += 1
        return
    for i in range(N):
        if not visit[k][i]:
            check(k, i, 1, 2)
            queen(k+1)
            check(k, i, 0, -2)

def check(y, x, v, w):
    global cnt
    visit[y][x] = v
    l = x
    r = x
    while y < N -1 :
        y += 1
        l -= 1
        r += 1
        visit[y][x] += w
        if l >= 0:
            visit[y][l] += w
        if r < N:
            visit[y][r] += w


N = int(sys.stdin.readline())

cnt = 0
visit = [[0] * N for _ in range(N)]

queen(0)
print(cnt)
