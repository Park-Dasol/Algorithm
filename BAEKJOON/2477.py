K = int(input())
check = [0]*5
info = [list(map(int, input().split())) for _ in range(6)]

for i in range(6):
    if info[i % 6][0] == info[(i+2) % 6][0] and info[(i+1) % 6][0] == info[(i-1) % 6][0]:
        area = info[(i+3) % 6][1] * info[(i-2) % 6][1] - info[(i+1)%6][1]* info[i % 6][1]
print(area*K)


