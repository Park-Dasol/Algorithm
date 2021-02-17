import sys

def getMin(k, s, b):
    global minPrice
    if k >= N:
        if s < minPrice:
            minPrice = s
        else:
            return
    if s >= minPrice:
        return
    mval = 489239320
    midx = b
    for i in range(3):
        if prices[k][i] <= mval and i != b:
            mval = prices[k][i]
            midx = i
    getMin(k + 1, s + prices[k][midx], midx)

        # if i != b:
        #     getMin(k+1, s + prices[k][i], i)


N = sys.stdin.readline()
N = int(N)
prices = [list(map(int, input().split())) for _ in range(N)]
minPrice = 393834884829329328

for i in range(3):
    getMin(1, prices[0][i], i)
print(minPrice)
