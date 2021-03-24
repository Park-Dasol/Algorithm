

T = int(input())

for i in range(1, T+1):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0
    k = 1
    dissum = 0
    while dissum < distance:
        cnt += 1
        dissum += k
        if cnt % 2 == 0:
            k += 1
    print(cnt)


