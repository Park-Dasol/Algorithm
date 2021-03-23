def game(v, i):
    visit[v] = 1

    for w in nums:
        if visit[w] == 0:
            game(w, i)
        elif visit[w] and w== i:
            result.append(w)




N = int(input())

nums = [0]
for i in range(N):
    nums.append(int(input()))
result = []
for i in range(N+1):
    visit = [0] * (N+1)
    game(i, i)

print(len(result))
for i in range(len(result)):
    print(result[i])