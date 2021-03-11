import pprint

# y,x 위치안에서 가능한 d1, d2 길이를 구해 다른 함수를 호출
def border(y, x):
    global visit
    for i in range(1, x +1):
        for j in range(1, min(N-x, N-y-i)):
            section(i, j, y, x)
            get_five(i, j, y, x)
            get_val()

# 각 구역의 인구수를 조사하고 최대값과최소값의 최소값을 구한다.
def get_val():
    global visit, minVal
    area = [0]*5
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 1:
                area[0] += matrix[i][j]
            elif visit[i][j] == 2:
                area[1] += matrix[i][j]
            elif visit[i][j] == 3:
                area[2] += matrix[i][j]
            elif visit[i][j] == 4:
                area[3] += matrix[i][j]
            else:
                area[4] += matrix[i][j]
    # print(area)
    gap = max(area) - min(area)
    if gap < minVal:
        minVal = gap

# 반복문을 돌면서 1,2,3,4구역에 영역을 표시한다.
def get_five(d1, d2, y, x):
    for i in range(N):
        flag = 1
        left = 1
        right = 2
        for j in range(N):
            # 중간에 왼쪽은 3, 오른쪽으로 4로 바꿔준다.
            if i > y + d2 and j >= x + d2 -d1 :
                right = 4
            if i >= y + d1 :
                left = 3

            # x행보다 작거나 같은경우 1(left), 2(right)
            if i <= y and visit[i][j] == 0 :
                if j <= x :
                    visit[i][j] = left
                else :
                    visit[i][j] = right
            # 5구역이 한행이 2개이상있는 지역부터는
            # flag를 써서 5 나타나기전 5 등장 후, 5가 2번 등장 후로 나누어 입력한다.
            elif i < y + d1 + d2:
                if visit[i][j] == 5:
                    if flag:
                        flag = 0
                    else :
                        flag = 2
                if visit[i][j] == 0 and flag == 1:
                    visit[i][j] = left
                elif visit[i][j] == 0 and flag == 2:
                    visit[i][j] = right
            # 5구역이 끝나는 행
            elif i >= y + d1 + d2 and visit[i][j] == 0:
                if j < x + d2 - d1:
                    visit[i][j] = left
                else :
                    visit[i][j] = right


# 4가지 방향을 돌면서 5번재 구역의 경계를 나누는 함수
def section(d1, d2, y, x):
    global visit
    visit = [[0] * N for _ in range(N)]
    for dir in range(4):
        if dir % 2 :
            l = d1
        else :
            l = d2
        for i in range(l):
            newy = y + dy[dir]
            newx = x + dx[dir]
            visit[newy][newx] = 5
            y = newy
            x = newx

    # 1 <= d1 <= y, 1<= d2 < N-x,



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]
visit = [[0]*N for _ in range(N)]
minVal = 82438957298342938478987923

# x,y과 움직일수 있는 범위안에서 border함수로 보내준다.
for i in range(0, N-2):
    for j in range(1, N-1):
        # i + di <= N, j + dj < N
        #0 ≤ y < y+d1+d2 <= N, 0 ≤ x-d1 < x < x+d2 < N
        border(i, j)



print(minVal)