import pprint

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

info.insert(0, [0, 0])
# W (무게), V(가치)
visit = [[0]* (K+1) for _ in range(N+1)]

# print(info)

for i in range(N+1):
    for j in range(K +1):
        if info[i][0] <= j :
            visit[i][j] = max(visit[i-1][j-info[i][0]] + info[i][1], visit[i-1][j])
        else:
            visit[i][j] = visit[i-1][j]

print(visit[N][K])
# pprint.pprint(visit)