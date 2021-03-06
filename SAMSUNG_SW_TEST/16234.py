def openhouse(i, j):
    global cnt
    pointer = -1
    lst.append((i, j))
    visit[i][j] = cnt
    while pointer < len(lst)-1:
        #포인터를 하나씩 증가해가면서 lst를 탐색한다.
        pointer += 1
        (y, x) = lst[pointer]
        # 네가지 방향을 돌면서 국경을 개방할 수있는 지역을 lst에 추가한다.
        for dir in range(4):
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newy >= 0 and newy < N and newx >= 0 and newx < N :
                gap = abs(nations[y][x] - nations[newy][newx])
                if visit[newy][newx] == 0 and gap >= L and gap <= R:
                    visit[newy][newx] = cnt
                    # 방문할 지역을 lst에 붙여준다.
                    lst.append((newy, newx))



def check_flag():
    for i in range(N):
        for j in range(N):
            gap1 = R + 100
            gap2 = R + 100
            # 반복문을 돌면서 오른쪽과 아래쪽을 비교해서 문을 열수 있는지 확인한다
            if i + 1 < N:
                gap1 = abs(nations[i][j] - nations[i+1][j])
            if j + 1 < N :
                gap2 = abs(nations[i][j] - nations[i][j+1])
            if (gap1 >= L and gap1 <= R) or (gap2 >= L and gap2 <= R):
                #국경을 열수 있으면 True를 리턴한다.
                return True
    return False

N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
cnt =0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
lst = []
t = 0

# 국경이 열릴때마다 while문을 돈다.
# check_flag 함수로 국경을 열지 확인한다.
while check_flag():
    # while문을 한번 돌때마다 국경을 열고 이것은 변수t로 숫자를 센다.
    t += 1
    for l in range(N):
        for j in range(N):
            if visit[l][j] == 0 :
                #visit 이 0인 지역을 발견할때마다cnt를 하나씩 증가시킨다.
                cnt += 1
                # i, j 지역이 열릴때 열리는 지역을 확인하기 위해서 openhouse 함수로 확인한다.
                openhouse(l, j)
                temp = 0

                my_set = set(lst)
                my_list = list(my_set)
                # i, j 지역에서 열리는 나라들의 값을 temp에 더하고 그 리스트 길이로 나눠 평균값을 구한다.
                for i in range(len(my_list)):
                    (r, c) = my_list[i]
                    temp += nations[r][c]
                val = temp // len(my_list)
                # 구한평균값을 대입해준다.
                for i in range(len(my_list)):
                    (r, c) = my_list[i]
                    nations[r][c] = val
                lst = []
    # visit 초기화한다.
    visit = [[0]*N for _ in range(N)]
print(t)