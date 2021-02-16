def getMin(k, s, b):
    global minPrice
    if k >= N:
        if s < minPrice:
            minPrice = s
        else:
            return
    if s >= minPrice:
        return
    for i in range(3):
        if i != b:
            getMin(k+1, s + prices[k][i], i)


N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]
minPrice = 393834884829329328

getMin(0, 0, 41)
print(minPrice)
