import sys
sys.setrecursionlimit(100000)

def blind(i, j, c):
    for dir in range(4):
        newy = i + dy[dir]
        newx = j + dx[dir]
        if newy >= 0 and newy < N and newx >= 0 and newx< N:
            if visit[newy][newx] == 0:
                if matrix[newy][newx] == c:
                    visit[newy][newx] = 1
                    blind(newy, newx, c)
                elif c in ['R', 'G'] and matrix[newy][newx] in ['R', 'G']:
                    visit[newy][newx] = 1
                    blind(newy, newx, c)

def people(i, j, c):
    for dir in range(4):
        newy = i + dy[dir]
        newx = j + dx[dir]
        if newy >= 0 and newy < N and newx >= 0 and newx< N:
            if visit[newy][newx] == 1:
                if matrix[newy][newx] == c:
                    visit[newy][newx] = 0
                    people(newy, newx, c)



N = int(sys.stdin.readline())
matrix = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
blind_cnt = 0
people_cnt = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            blind_cnt += 1
            visit[i][j] = 1
            blind(i, j, matrix[i][j])

for i in range(N):
    for j in range(N):
        if visit[i][j] == 1:
            people_cnt += 1
            visit[i][j] = 0
            people(i, j, matrix[i][j])


print(people_cnt, blind_cnt)

