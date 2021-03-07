#미세먼지 확산 함수
def spread():
    #매초 visit 함수를 초기화한다.
    visit = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            dust = matrix[i][j]
            # 미세먼지값이 0보다 클때만 확산을 수행한다.
            if dust > 0 :
                val = dust // 5
                for dir in range(4):
                    newy = i + dy[dir]
                    newx = j + dx[dir]
                    # 네군데 방향을 돌며 그 위치가 공기청정기가 아니고, 집 안의 공간일때마다
                    if newy>= 0 and newy < R and newx >=0 and newx < C and matrix[newy][newx] >=0:
                        # 원래 미세먼지 위치에서 val(dust//5)를 빼고
                        # 그 이웃자리에 미세먼지를 확산하도록 visit 이차원 배열에 그 값을 담아준다.
                        visit[newy][newx] += val
                        visit[i][j] -= val
    # visit 이차원 배열과 matrix 이차원 배열의 각 원소의 합을 더해서 미세먼지 확산을 완료한다.
    for i in range(R):
        for j in range(C):
            matrix[i][j] += visit[i][j]


# 공기청정기로 미세먼지 흡입 하는 함수
def clean():
    # 공기청정기의 상단부와 하단부의 위치 설정
    top = cleaner[0]
    bottom = cleaner[1]
    # 0번째 열의 공기청정기 상단부는 한칸씩 아래로 먼지가 이동
    for i in range(top-1, -1, -1):
        matrix[i+1][0] = matrix[i][0]
    # 0번째 열의 공기청정기 하단부는 한칸씩 위로 먼지가 이동
    for i in range(bottom+ 1, R):
        matrix[i-1][0] = matrix[i][0]
    # 공기청정기 자리는 다시 -1로 바꿔준다.
    matrix[top][0] = -1
    matrix[bottom][0] = -1
    # 방의 0번째 행과 R-1번째행은 0번째 열의 값을 빼고 맨 뒤에 0으로 값을 채워준다.
    matrix[0].pop(0)
    matrix[R-1].pop(0)
    matrix[0].append(0)
    matrix[R-1].append(0)
    # C-1번째 열의 공기청정기 하단부는 한칸씩 아래로 먼지가 이동
    for i in range(R-1, bottom, -1):
        matrix[i][C-1] = matrix[i-1][C-1]
    # C-1번째 열의 공기청정기 상단부는 한칸씩 위로 먼지가 이동
    for i in range(0, top):
        matrix[i][C-1] = matrix[i+1][C-1]
    # 공기청정기 자리는 다시 -1로 바꿔준다.
    matrix[top][0] = -1
    matrix[bottom][0] = -1
    # 공기청정가 상단부열과 하단부열의 R-1 열의 값을 빼고, 1번째 열에 0을 채워준다.
    matrix[top].pop()
    matrix[bottom].pop()
    matrix[top].insert(1,0)
    matrix[bottom].insert(1,0)


R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
visit = [[0] * C for _ in range(R)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
cleaner = []
#공기청정기의 위치를 찾는다
for i in range(R):
    if matrix[i][0] == -1 :
        cleaner.append(i)

# 1초마다 while문을 돌며 미세먼지 확산과 공기청정기로 청소를 반복한다.
while T > 0:
    T -= 1
    spread()
    clean()

res =0


# 남아있는 미세먼지의 양 계산
for r in range(R):
    for c in range(C):
        if matrix[r][c] >= 0:
            res += matrix[r][c]
print(res)