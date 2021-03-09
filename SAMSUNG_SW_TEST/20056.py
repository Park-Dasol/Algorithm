# move 함수는 볼이 이동한 위치를 기록해준다.
def move(r, c, m, s, d):
    # s * d만큼 이동하는데 N보다 크면 원형큐처럼 돌아오기 때문에
    # s를 N으로 나눈 것에다가 dis를 곱해서 거리를 측정하고
    # 방향이 -일수도 있으므로 N을 더한후  N으로 나눈 나머지만큼 이동해준다.
    dis = s % N

    newy = ( r + (dy[d] * dis) + N ) % N
    newx = ( c + (dx[d] * dis) + N ) % N
    next = matrix[newy][newx]

    # 이미방문했던 위치라면 전에 방문했던 파이어볼이랑 방향이
    # 홀짝여부를 체크한다. 그리고 다르면 4번인덱스에 1을 적어줌
    if next[3]:
        if next[2] % 2 != d % 2:
            matrix[newy][newx][4] = 1
    # 파이어볼의 이동한 위치에 m, s, d를 업데이트 해주고, c는 그곳에 존재하는 파이어볼 수를 1 더해준다.
    matrix[newy][newx][0] += m
    matrix[newy][newx][1] += s
    matrix[newy][newx][2] = d
    matrix[newy][newx][3] += 1




N, M, K = map(int, input().split())
# m, s, d, c, bool
matrix = [[[0]*5 for _ in range(N)] for _ in range(N)]
info = []
# 방향키
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
# 입력받은 파이어볼 정보를 info에 담음
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    info.append([r-1, c-1, m, s, d])



# K번 이동한다
for k in range(K):
    #matrix에는 방문 정보를 담는다.
    matrix = [[[0] * 5 for _ in range(N)] for _ in range(N)]
    # info리스트에서 볼이 있는 곳마다 move 함수를 돌린다.
    for l in info:
        move(l[0], l[1], l[2], l[3], l[4])
    # m, s, d, cnt, bool
    info = []
    # move 함수를 다녀온후 info 리스트를 비워준후
    # for문을 돌며 info 에 다시 파이어볼을 담는다.
    for i in range(N):
        for j in range(N):
            ball = matrix[i][j]
            #파이어볼이 하나 있으면 그걸 info에 담는다.
            if ball[3] ==1:
                info.append([i, j, ball[0], ball[1], ball[2]])
            # 파이어볼이 여러개 있으면
            elif ball[3] > 1:
                ball = matrix[i][j]
                # 파이어볼 무게의 합을 5로 나눈 몫을 w로 지정
                # 파이어볼 속도의 합을 파이어볼수로 나눈 값을 s로 지정
                w = ball[0] // 5
                s = ball[1] // ball[3]
                # 네가지의 다른 방향값을 정해준다.
                for dir in range(4):
                    #한곳에 있는 여러개의 파이어볼이 모두 방향이 홀수이거나 짝수라면
                    # 0, 2, 4, 6 방향으로
                    if matrix[i][j][4]==0:
                        dir = dir * 2
                    # 파이어볼이 홀짝수 방향이 섞였다면, 1, 3, 5, 7 방향으로 흩어진다.
                    else:
                        dir = dir * 2 + 1
                    # 분열될 파이어볼이 0보다 크다면 info리스트에 담아준다.
                    if w > 0:
                        info.append([i, j, w, s, dir])

# 남은 info 리스트의 볼의 무게를 다 더한후 출력한다.
res = 0
for z in info:
    res += z[2]
print(res)

