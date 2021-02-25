def rotate(N, d):
    visit = [0] * 4
    visit[N] = d
    #왼쪽오른쪽을 탐색하며 회전시킬 톱니바퀴를 visit에 표시한다.
    if N > 0 : # 왼쪽탐색
        for i in range(N-1, -1, -1):
            if visit[i+1] != 0:
                if gear[i+1][pointer[i+1][1]] == gear[i][pointer[i][0]]:
                    break
                else:
                    visit[i] = visit[i+1] * (-1)


    if N < 3: # 오른쪽탐색
        for i in range(N+1, 4):
            if visit[i-1] != 0:
                if gear[i-1][pointer[i-1][0]] == gear[i][pointer[i][1]]:
                  break
                else:
                    visit[i] = visit[i-1] * (-1)
    # visit를 탐색하며 톱니바퀴의 포인터를 바꿔준다.
    for i in range(4):
        # 회전시 포인터는 그 반대방향으로 회전하므로 -1을 곱해준다.
        pointer[i][0] = (pointer[i][0] + visit[i]*(-1) + 8 ) % 8
        pointer[i][1] = (pointer[i][1] + visit[i]*(-1) + 8) % 8


gear = [list(map(int, input())) for _ in range(4)]
pointer = [[2, 6] for _ in range(4)]

# 왼쪽 닿는부분 6번, 오른쪽 닿는 부분 2번
K = int(input())
for i in range(K):
    N, d = map(int, input().split())
    rotate(N-1, d)


res = 0
for j in range(4):

    idx = (pointer[j][1] + 2) % 8
    res += gear[j][idx] * (2 ** j)

print(res)