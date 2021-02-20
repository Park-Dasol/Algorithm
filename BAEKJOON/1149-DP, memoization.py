
N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]

visit = [[100000000000]*3 for _ in range(N)]
k = 0
while k < N :
    if k == 0 :
        for i in range(3):
            visit[k][i] = prices[k][i]
    else :
        for i in range(3): # 현재 줄
            for j in range(3): # 전의 줄
                if i != j and visit[k-1][j] + prices[k][i] <= visit[k][i]:
                    visit[k][i] = visit[k-1][j] + prices[k][i]

    k += 1
print(min(visit[N-1]))






