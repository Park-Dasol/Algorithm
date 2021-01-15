N = int(input())
cal = [0] * 366
for i in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        cal[i] += 1
depth = 0
length = 0
tape = []
for i in range(366):
    if cal[i] > 0:
        length += 1
        if cal[i] > depth:
            depth = cal[i]
        if i == 365:
            tape.append([length, depth])
    else:
        if cal[i-1] > 0 :
            tape.append([length, depth])
        length = 0
        depth = 0


res = 0
for i in range(len(tape)):
    res += tape[i][0] * tape[i][1]
print(res)
