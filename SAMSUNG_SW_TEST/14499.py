def game(x, y):
    for dir in order:
        newy = y + dy[dir]
        newx = x + dx[dir]
        if newy >= 0 and newy < M and newx >= 0 and newx < N:
            res = move(newy, newx, dir)
            x = newx
            y = newy
            print(res)
        else:
            continue


def move(newy, newx, dir):
    if dir == 1:
        dice['top'], dice['east'], dice['bottom'], dice['west'] = dice['west'], dice['top'], dice['east'], dice['bottom']
    elif dir == 2:
        dice['top'], dice['west'], dice['bottom'], dice['east'] = dice['east'], dice['top'], dice['west'], dice['bottom']
    elif dir == 3:
        dice['top'], dice['north'], dice['bottom'], dice['south'] = dice['south'], dice['top'], dice['north'], dice['bottom']
    else :
        dice['top'], dice['south'], dice['bottom'], dice['north'] = dice['north'], dice['top'], dice['south'], dice['bottom']

    if board[newx][newy] == 0:
        board[newx][newy] = dice['bottom']
    else :
        dice['bottom'] = board[newx][newy]
        board[newx][newy] = 0
    return dice['top']



N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = {'top': 0, 'bottom':0, 'east':0, 'west':0, 'north':0, 'south':0}

#0, 동, 서, 남, 북
dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, -1, 1]

game(x, y)
