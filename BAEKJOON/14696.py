T = int(input())
for tc in range(1, T+1):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    #star : 4, round : 3, rectangle:2, triangle:1
    cntA = [0] * 5
    cntB = [0] * 5

    lenA = A.pop(0)
    lesB = B.pop(0)
    for a in A:
        cntA[a] += 1
    for b in B:
        cntB[b] += 1
    idx = 5
    while idx != 0:
        idx -= 1
        if cntA[idx] > cntB[idx]:
            res = 'A'
            break
        elif cntA[idx] < cntB[idx]:
            res = 'B'
            break
        else:
            res = 'D'
    print(res)



