def get_ans(start, idxH, k):
    global result
    s = 0
    cnt = 0
    for j in range(start, idxH, k):
        if j == idxH -1*k:
            if s < visit[j]:
                result += cnt *s
                result += visit[j]
            else:
                cnt += 1
                result += cnt * s
            break
        if visit[j] > s:
            result += cnt * s
            cnt = 1
            s = visit[j]
        else:
            cnt += 1


N= int(input())
visit = [0] *1001

maxH = 0
maxL = 0
for i in range(N):
    L, H = map(int, input().split())
    if H > maxH:
        maxH = H
        idxH = []
    if H == maxH:
        idxH.append(L)

    if L > maxL:
        maxL = L
    visit[L] = H

result = 0

if len(idxH) == 1:
    left = idxH[0]
    right = idxH[0]
    result += maxH
else:
    left = min(idxH)
    right = max(idxH)
    result += (right-left+1) * maxH


if right != maxL:
    get_ans(maxL, right, -1)


if left != 0:
    get_ans(0, left, 1)


print(result)


