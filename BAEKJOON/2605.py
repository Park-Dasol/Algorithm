N = int(input())
randumnum = list(map(int, input().split()))
lineup = [0] * N
for i in range(N-1, -1, -1):
    n = 0
    k = 0
    while n <= randumnum[i]:
        if lineup[k] != 0:
            k += 1
            continue
        else:
            k += 1
            n += 1
        # if lineup[k] != 0:
        #     n += 1
        #     k += 1
        # else:
        #     k += 1
    lineup[k-1] = i+1
result = lineup[::-1]
for i in result:
    print(i, end=' ')