import sys

lstck = list(sys.stdin.readline().rstrip())
rstck = []
M = int(sys.stdin.readline().rstrip())


for i in range(M):
    C = list(sys.stdin.readline().split())
    if C[0] == 'P':
        lstck.append(C[1])
    elif C[0] == 'L' and lstck:
        rstck.append(lstck.pop())
    elif C[0] == 'D' and rstck:
        lstck.append(rstck.pop())
    elif C[0] == 'B' and lstck:
        lstck.pop()

print(''.join(lstck) + ''.join(rstck[::-1]))
