import sys

def auction(k, p, c, n):
    global cnt
    if cnt < c:
        cnt = c
    if cnt == N:
        return
    if n >= N:
        return

    for i in range(N):
        if visit[i] == 0 and matrix[k][i] >= p:
            visit[i] = 1
            auction(i, matrix[k][i], c + 1, n+1)
            visit[i] = 0
    n += 1

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visit = [0] * N
cnt = 1
visit[0] = 1
auction(0, 0, 1, 0)
print(cnt)


'''
7
0333456
1024000
2304007
2040507
3456000
4007008
4500000



10
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000

'''