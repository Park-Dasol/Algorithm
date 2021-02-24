N = int(input())
nums = list(map(int, input().split()))
B, C = map(int, input().split())
res = N
for i in nums:
    if i >= B:
        res += (i - B) // C
        if (i-B) % C:
            res += 1
    else:
        continue
print(res)


