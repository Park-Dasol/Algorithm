
import sys


# players = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(30)]

def fight(b, w, k, p):
    global N, record, gap
    if b >= 15 and w >= 15:
        if record < p:
            record = p
        return
    if k >= N:
        return
    if b < 15:
        fight(b+1, w, k + 1, p + players[k][1])
    if w < 15:
        fight(b, w+1, k + 1, p + players[k][0])
    if gap > 0:
        gap -= 1
        fight(b, w, k + 1, p)





players = []

for line in sys.stdin:
    a = list(map(int, line.split()))
    players.append(a)
# a = [1]
# while len(a)> 0:
#     a = list(map(int, input().split()))
#     players.append(a)
# N = len(players)
# N = 31
gap = N - 30
record = 0
fight(0, 0, 0, 0)

print(record)



#
# players = []
# a= ['a']
# while len(a)> 0:
#     players.append(a)
#     a = list(map(int, input().split()))
# N = len(players)
# gap = N - 31
# record = 0
# fight(0, 0, 1, 0)
# print(record)
#
#
print(players)
# print(N)