def get_score(visit):
    global min_gap
    if visit.count(1) == N or visit.count(0) == N:
        return
    total_A = 0
    total_B = 0
    for i in range(N):
        for j in range(N):
            if i != j and visit[i] == visit[j]:
                if visit[i] == 0:
                    total_A += matrix[i][j]
                else:
                    total_B += matrix[i][j]
    if abs(total_A- total_B) < min_gap:
        min_gap = abs(total_A - total_B)





N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
min_gap = 9032892982489982389

for i in range(1 <<N):
    visit = []
    for j in range(N):
        if i & (1 << j):
            visit.append(1)
        else:
            visit.append(0)
    get_score(visit)

print(min_gap)