w, h = map(int, input().split()) # w = y , h = x
p, q = map(int, input().split()) # p = y, q = x
t = int(input())

if t >= w-p:
    temp = t - (w-p)
    mok = temp // w
    nameoji = temp % w
    if mok % 2 :
        flag = 1
    else :
        flag = 0
    if flag == 0:
        y = w - nameoji
    else:
        y = nameoji
else:
    y = w + t

if t >= h-q:
    temp = t - (h-q)
    mok = temp // h
    nameoji = temp % h
    if mok % 2 :
        flag = 1
    else:
        flag = 0

    if flag == 0:
        x = h - nameoji
    else:
        x = nameoji
else:
    x = h + t


print(y, x)


