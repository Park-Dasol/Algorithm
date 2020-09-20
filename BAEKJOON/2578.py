def bingo():
    global cnt
    cnt = 0
    for i in range(5):
        for j in range(5):
            cnt += 1
            n = numbers[i][j]
            if findnum(n):
                return cnt

def findnum(n):
    global cnt
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == n:
                visit[i][j] = 1
                if check(i, j):
                    return True
                else:
                    return False

def check(x, y):
    for i in range(5):
        flag = 0
        if bx[i] == 0:

            for j in range(5):
                if visit[i][j] == 0:
                    break
                else:
                    flag += 1
            if flag == 5:
                bx[i] = 1
    for j in range(5):
        flag = 0
        if by[j] == 0 :
            for i in range(5):
                if visit[i][j] == 0:
                    break
                else:
                    flag += 1
            if flag == 5:
                by[j] = 1
    if brl[0] == 0:
        flag = 0
        for i in range(5):
            if visit[i][i] == 1:
                flag += 1
        if flag == 5:
            brl[0] =1
    if brl[1] == 0:
        flag = 0
        for i in range(5):
            if visit[i][4-i] == 1:
                flag += 1
        if flag == 5:
            brl[1] =1
    line = 0
    for i in range(5):
        if bx[i] ==1 :
            line += 1
        if by[i] == 1:
            line += 1
    for i in range(2):
        if brl[i] == 1:
            line += 1
    if line >= 3:
        return True
    else:
        return False






matrix = [list(map(int,input().split())) for _ in range(5)]
numbers = []
numorder = [numbers.append(list(map(int,input().split())))for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
bx = [0] * 5
by = [0] * 5
brl = [0] *2
print(bingo())


