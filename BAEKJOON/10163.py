N = int(input())
info = [0] * N
matrix = [[0]* 101 for _ in range(101)]
for n in range(1, N+1):
    x, y, width, height = map(int, input().split())
    for i in range(x, x + width):
        for j in range(y, y + height):
            matrix[i][j] = n
for n in range(1, N+1):
    cnt = 0
    for i in range(101):
        for j in range(101):
            if matrix[i][j] == n:
                cnt += 1
    print(cnt)


