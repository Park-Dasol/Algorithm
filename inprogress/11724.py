
def dfs(i):
    visit[i] = 1
    for w in range(1, N+1):
        if mat[i][w] == 1 and visit[w] == 0 :
            dfs(w)


N, M = map(int, input().split())
mat = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    mat[s][e] = 1
    mat[e][s] = 1
visit = [0] * (N+1)
cnt = 1
dfs(1)
for v in range(1, N+1):
    if visit[v] == 0:
        cnt += 1
        dfs(v)
print(cnt)