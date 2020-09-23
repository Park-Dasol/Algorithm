N= int(input())
nums = list(map(int,input().split()))
i = 1
maxi = 1
for n in range(N-1):
    if nums[n] <= nums[n+1]:
        i += 1
        if i >= maxi:
            maxi = i
    else:
        i = 1
i = 1
for n in range(N-1):
    if nums[n] >= nums[n+1]:
        i += 1
        if i >= maxi:
            maxi = i
    else:
        i = 1

print(maxi)