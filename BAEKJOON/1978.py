import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

cnt = [0] * len(lst)
s = 1
for i in range(len(lst)):
    for j in range(1, lst[i]+1):
        if lst[i] % j == 0:
            cnt[i] += 1
print(cnt.count(2))

