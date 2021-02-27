def chicken(k, cnt):
    global answer
    if cnt == M:
        dis = distance()
        if dis < answer:
            answer = dis
        return
    if k >= len(store):
        return
    if cnt > M:
        return
    visit[k] = 1
    chicken(k +1, cnt + 1)
    visit[k] = 0
    chicken(k+1, cnt)

def distance():
    dis = 0
    for i in house:
        hy, hx = i[0], i[1]
        dis_min = 1000
        for j in range(len(visit)):
            if visit[j] == 1:

                sy, sx = store[j][0], store[j][1]
                temp = abs(hy - sy) + abs(hx - sx)
                if temp < dis_min:
                    dis_min = temp
            else:
                continue
        dis += dis_min
    return dis



N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

answer = 238378489293328989
house = []
store = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2 :
            store.append([i, j])
        elif matrix[i][j] == 1 :
            house.append([i, j])

visit= [0]* len(store)
chicken(0, 0)

print(answer)