def color(x,y):
    global cnt
    for i in range(x, x+10):
        for j in range(y, y+ 10):
            if matrix[i][j] == 0:
                cnt += 1
                matrix[i][j] =1




N = int(input())
cnt = 0
matrix = [[0]*100 for _ in range(100)]
for n in range(N):

    x, y = map(int,input().split())
    color(x,y)
print(cnt)