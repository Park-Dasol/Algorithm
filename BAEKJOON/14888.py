def get_cal(k, s):
    if k+1 >= len(nums):
        result.append(s)
        return

    for i in range(4):
        if operation[i] > 0:
            if i == 0 :
                operation[i] -= 1
                get_cal(k+1, s + nums[k+1])
                operation[i] += 1
            elif i == 1:
                operation[i] -= 1
                get_cal(k + 1, s - nums[k + 1])
                operation[i] += 1
            elif i == 2:
                operation[i] -= 1
                get_cal(k + 1, s * nums[k + 1])
                operation[i] += 1
            elif i == 3 :
                operation[i] -= 1
                if s < 0 and nums[k+1] >0 :
                    operated = s * (-1) // nums[k+1] * (-1)
                else:
                    operated = s // nums[k+1]
                get_cal(k + 1,operated)
                operation[i] += 1

N = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split()))
# +, - , *, % 순서
result = []
get_cal(0, nums[0])
print(max(result))
print(min(result))


