import pprint

def trip(y, x, dir):
    global cnt
    q = []
    q.append((y, x, dir))
    while q:
        flag = 0
        (y, x, dir) = q.pop(0)
        visit[y][x] += 1
        if dir < 2 :
            start = dir
            end = dir + 1
        else:
            start = 0
            end = 2
        for i in range(start, end):
            newy = y + dy[i]
            newx = x + dx[i]
            if newy == N-1 and newx == N-1:
                cnt += 1
            elif newy >= 0 and newy < N and newx >= 0 and newx < N and matrix[newy][newx] == 0:
                q.append((newy, newx, i))
            else:
                continue
        for i in range(3):
            newy = y + dy[i]
            newx = x + dx[i]
            if newy >= 0 and newy < N and newx >= 0 and newx < N and matrix[newy][newx] == 0:
                flag += 1
            else :
                break
        if flag == 3:
            if newy == N-1 and newx == N-1:
                cnt += 1
            else :
                q.append((newy, newx, i))



N= int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
y = 0
x = 1
tail = (0, 0)
dy = [0, 1, 1]
dx = [1, 0, 1]
cnt = 0
trip(y, x, 0)
pprint.pprint(visit)
print(cnt)


