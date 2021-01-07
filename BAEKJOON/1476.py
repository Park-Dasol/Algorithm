import sys
time = list(map(int, sys.stdin.readline().split()))
# print(time)
# E: 지구, S : 태양, M: 달
stan = [15, 28, 19]
i =0
j = 0
l =0
while i >= 0:
    while stan[0]* i + time[0] > stan[1] * j + time[1] :
        j += 1
        while stan[1] *j + time[1] > stan[2] * l + time[2]:
            l += 1
    if stan[0]* i + time[0] == stan[1] * j + time[1] and stan[2] * l + time[2] == stan[1] *j + time[1] :
        break
    i += 1
print(stan[0]* i + time[0])

