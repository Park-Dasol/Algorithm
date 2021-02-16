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
            # print(colors[i][k])
            getMin(k+1, s + colors[i][k], i)


N = int(input())

red = list(map(int, input().split()))
green = list(map(int, input().split()))
blue = list(map(int, input().split()))

colors = {0: red, 1: green, 2: blue}
minPrice = 393834884829329328

getMin(0, 0, 41)
print(minPrice)
