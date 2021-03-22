N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
visit = [[0] *N for _ in range(N)]
visit[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1 :
            print(visit[N - 1][N - 1])
            break
        cur = matrix[i][j]
        if j + cur < N:
            visit[i][j + cur] += visit[i][j]
        if i + cur < N:
            visit[i+ cur][j] += visit[i][j]
