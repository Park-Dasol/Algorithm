


N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1, 1 << len(nums)):
    b_total = 0
    for j in range(N):
        if i & 1 << j :
            b_total += nums[j]
    if b_total == S:
        cnt += 1
print(cnt)