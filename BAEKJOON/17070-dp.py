import pprint
N= int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[[0]*3 for _ in range(N+1)] for _ in range(N+1)]
visit[1][2] = [1, 0, 0]


dx = [-1, 0, -1]
dy = [0, -1, -1]

for i in range(1, N+1):
    for j in range(1, N+1):
        newy = i + dy[0]
        newx = j + dx[0]
        if (visit[newy][newx][0] > 0 or visit[newy][newx][2] > 0) and matrix[i-1][j-1] != 1 :
            visit[i][j][0] = visit[newy][newx][0] + visit[newy][newx][2]
        newy = i + dy[1]
        newx = j + dx[1]
        if (visit[newy][newx][1] > 0 or visit[newy][newx][2] > 0) and matrix[i-1][j-1] != 1 :
            visit[i][j][1] = visit[newy][newx][1] + visit[newy][newx][2]
        newy = i + dy[2]
        newx = j + dx[2]
        if sum(visit[newy][newx]) != 0 and matrix[i-1][j-1] != 1 and matrix[i-2][j-1] != 1 and matrix[i-1][j-2] != 1:
            visit[i][j][2] = sum(visit[newy][newx])

print(sum(visit[N][N]))
