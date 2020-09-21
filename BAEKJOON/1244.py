def boy(k):
    for i in range(len(switch)):
        if (i+1) % k == 0:

            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0

def girl(k):
    n = 0
    if switch[k] == 1:
        switch[k] = 0
    else:
        switch[k] = 1
    while n <= len(switch):
        n += 1
        if 0<= k-n < len(switch) and 0<= k+n < len(switch) and switch[k-n] == switch[k+n]:
            if switch[k-n] == 1:
                switch[k-n] = 0
                switch[k+n] = 0
            else:
                switch[k-n] = 1
                switch[k+n] = 1

        else:
            break


N = int(input())
switch = list(map(int, input().split()))
S = int(input())
for s in range(S):
    gender, key = map(int, input().split())
    if gender == 1:
        boy(key)
    else:
        girl(key-1)

n = 0
while n <= len(switch) :
    if n + 20 > len(switch):
        for i in range(len(switch)-n):
            print(switch[n+i],end=' ')
    else:
        for i in range(20):
            print(switch[n+i], end=' ')
    print()
    n += 20

