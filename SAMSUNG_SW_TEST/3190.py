def area_check(y, x):
    # 보드 바깥으로 나갔는지 확인하고 나갔으면 False를 리턴
    if y >= 0 and y <N and x >= 0 and x < N:
        # 자신의 몸과 부딪히는 영역인지확인하고 나가면 false 리턴
        for i in snake:
            if [y, x] == i :
                return False
        # 사과를 먹으면 사과자리만큼 길어지고, 사과를 0으로 없앤다.
        if board[y][x] == 1:
            snake.insert(0, [y, x])
            board[y][x] =0
            return True
        # 사과가 없으면 사과자리로 머리 이동하고 꼬리는 한칸 짧아진다.
        elif board[y][x] == 0 :
            snake.insert(0, [y, x])
            snake.pop()
            return True
    else :
        return False


def game():
    t = 0
    idx = 0
    #입력받은 방향정보에 따라 while 문을 돈다
    for i in range(len(directions)):
        X = directions[i][0]
        X = int(X)
        C = directions[i][1]
        #t가 X가 될때까지
        while t != X :
            t += 1

            newy = snake[0][0] + dir[idx][0]
            newx = snake[0][1] + dir[idx][1]
            # 머리가 이동할 위치를 newy, newx 라고 하고 그곳에 대한 정보를 확인한다.
            if area_check(newy, newx):
                continue
            else:
                return t
        # X초가 되면 X초 후 방향을 전환해준다.
        if t == X:
            # 오른쪽회전 이면 idx를 +1
            if C == 'D':
                idx = (idx + 1) % 4
            # 왼쪽회전이면 idx를 -1
            elif C == 'L':
                idx = (idx + 3) % 4
    # 입력받은 방향정보가 끝났는데도 게임이 끝나지 않았을 경우에 대비해 또 돈다.
    # 직진만 가능하므로 최대 N 초를 돈다.
    n = N
    while n :
        n -= 1
        t+= 1
        newy = snake[0][0] + dir[idx][0]
        newx = snake[0][1] + dir[idx][1]
        if area_check(newy, newx):
            continue
        else:
            return t



N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

# 보드에 사과를 배치한다.
for i in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1
L = int(input())

# 뱀의 길이는 1, 위치는 0,0
snake = [[0, 0]]
#방향을 조절해줄 dir list 오른쪽회전일경우 인덱스를 +1, 왼쪽일 경우 -1 해준다.
dir = [[0,1], [1, 0], [0, -1], [-1, 0]]

#입력받을 방향 정보
directions = [list(map(str, input().split())) for _ in range(L)]


# 게임을 시작한다.
answer = game()
print(answer)

