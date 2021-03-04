import pprint

def clean(y, x, d):
    global cnt

    if matrix[y][x] == 0:

        matrix[y][x] = 2

    t = 4
    while t:
        t -= 1
        dir = (d + 3) % 4
        newy = y + dy[dir]
        newx = x + dx[dir]
        if area(newy, newx):
            if matrix[newy][newx] == 0 :
                clean(newy, newx, dir)
                return
        d = dir

    dir = (d + 2) % 4
    newy = y + dy[dir]
    newx = x + dx[dir]
    if wall(newy, newx):
        clean(newy, newx, d)
    else:
        return



def area(newy, newx):
    if newy >= 0 and newy < N and newx >= 0 and newx < M and matrix[newy][newx]==0:
        return True
    else :
        return False

def wall(newy, newx):
    if newy >= 0 and newy < N and newx >= 0 and newx < M and matrix[newy][newx] != 1:
        return True
    else:
        return False


N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]



dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
clean(r, c, d)

res = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            res += 1
print(res)



