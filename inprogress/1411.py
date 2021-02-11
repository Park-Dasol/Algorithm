import copy

N = int(input())
words = [list(map(str, input())) for _ in range(N)]
# print(words)
maxcnt = 1

# a: 97 z: 122
for i in range(N-1):
    visit = [0] * 27
    temp = copy.deepcopy(words)
    print(temp)
    cnt = 1
    for j in range(len(words[0])):
        for l in range(i+1, N):
            idx = ord(temp[i][j])- 97
            if temp[i][j] != temp[l][j] and visit[idx] != 1:
                visit[idx] = 1
                temp[l][j] = temp[i][j]
                if temp[i] == temp[l]:
                    cnt += 1
                if cnt > maxcnt:
                    maxcnt =cnt
print(maxcnt)
# print(ord('z')-ord('a'))