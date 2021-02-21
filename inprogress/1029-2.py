import sys

def auction(k, cnt, p):
    global maxCnt
    if not visit[k]:
        visit[k] = 1
    else :
        return

    if cnt > maxCnt:
        maxCnt = cnt

    for i in range(N):
        if matrix[k][i] >= p:
            auction(i, cnt + 1, matrix[k][i])
    visit[k] = 0

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visit = [0] * N
maxCnt = 1
auction(0, 1, 0)


print(maxCnt)