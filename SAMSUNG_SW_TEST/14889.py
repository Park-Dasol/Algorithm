def get_diff(powerset):
    global minS
    start = []
    link = []
    #부분집합의 값이 1인경우 start로, 0인 경우 link로 넣는다.
    for i in range(N):
        if powerset[i]:
            start.append(i)
        else:
            link.append(i)
    startS = 0
    linkS = 0
    #스타트팀의 능력치합과 링크팀 능력치합을 구한다.
    for i in range(0, n-1):
        for j in range(i+1, n):
            startS += matrix[start[i]][start[j]] + matrix[start[j]][start[i]]
            linkS += matrix[link[i]][link[j]] + matrix[link[j]][link[i]]
    #능력치의 차가 최소값인지 확인한다.
    if abs(startS - linkS) < minS:
        minS = abs(startS - linkS)





N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
n = N //2
minS = 100*N
#부분집합을 이용해 팀을 나눈다.
for i in range(1<<N):
    powerset = [0]*N
    cnt = 0
    for j in range(N):
        if i & (1<<j):
            powerset[j] = 1
            cnt += 1
    # 최소능력치가 0이 아닌경우, 팀의 인원이 절반vs절반으로 나뉠경우만 함수로 보낸다.
    if cnt == n and minS:
        get_diff(powerset)

print(minS)