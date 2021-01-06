import sys
n= int(input())
s = []
seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
i = 1
j = 0
res = []
while s or i <= n:
    if s and s[-1] == seq[j]:
        s.pop()
        res.append('-')
        j += 1
    else:
        s.append(i)
        res.append('+')
        i += 1
    if i > n+1 :
        res = ['NO']
        break
for i in res:
    print(i)



