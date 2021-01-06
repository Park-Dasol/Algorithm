T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    res = 0
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            res = i * (A // i) * (B // i)
            break

    print(res)

