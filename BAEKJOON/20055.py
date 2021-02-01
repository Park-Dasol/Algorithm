def get_count(num):
    if num < 0 :
        num = len(con) -1
    elif num >= len(con):
        num %= len(con)
    return num

N, K = map(int, input().split())
con = list(map(int, input().split()))
visit = [False] * (2*N)
up = 0
j = 0
while K > 0 :
    up -= 1
    j += 1
    up = get_count(up)
    if con[up] > 0:
        con[up] -= 1
        visit[up] = True

    for i in range(N, -1, -1):
        idx = get_count(up + i)
        if i == 0:
            if con[idx] == 0 and visit[idx] == True:
                K -= 1
        elif i == N -1:
            visit[idx] = False
        else:
            next = get_count(idx + 1)
            if visit[idx] and con[next] > 0 and (visit[next] == False or i == N - 2):
                visit[idx] = False
                visit[next] = True
                if i == N -2:
                    visit[next] = False
                con[next] -= 1
                if con[next] == 0:
                    K -= 1

print(j)
