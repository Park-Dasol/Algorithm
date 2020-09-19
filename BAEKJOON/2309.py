import copy
def get7(k, cnt):
    if cnt == 7:
        setsum(powerset)
        return

    if k == 9:
        return
    powerset[k] = 1
    get7(k+1, cnt +1)
    powerset[k] = 0
    get7(k+1, cnt)

def setsum(powerset):
    total = 0
    global result
    for i in range(9):
        if powerset[i] == 1:
            total += little[i]
    if total == 100:
        result = copy.deepcopy(powerset)
    return


little = []
powerset = [0]*9
cnt = 0
result = []
for i in range(9):
    nanjang = int(input())
    little.append(nanjang)
little.sort()
get7(0, cnt)
for i in range(9):
    if result[i] == 1:
        print(little[i])

