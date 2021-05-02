H, W = map(int,input().split())
nums = list(map(int, input().split()))



top = max(nums)
left = 0
right = 0
total = 0
topIdx = -1
for num in range(len(nums)) :
    i = nums[num]
    if i != top and i > left :
        left = i
        total += i
    elif i != top :
        total += left
    else :
        topIdx = num
        break

for num in range(len(nums)-1, -1, -1):
    i = nums[num]
    if i != top and i > right :
        right = i
        total += i
    elif i != top :
        total += right
    else :
        if topIdx ==num:
            total += i
            break
        else :
            total += (num-topIdx+1) * top
            break

print(total - sum(nums))
