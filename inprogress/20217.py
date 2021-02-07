N = int(input())
nums = list(map(int, input().split()))
sign = []
for n in range(len(nums)-1):
    if nums[n] > nums[n+1]:
        sign.append("-")
    elif nums[n] < nums[n+1]:
        sign.append("+")
    else:
        sign.append("0")

first = [0, 'sign']
second = [0, 'sign']
third = [0, 'sign']
flag = 'first'
zero = False

for s in sign:
    if flag == 'first' :
        if s == first[1] or s == '0':
            first[0] += 1
        elif first[1] == 'sign':
            first[0] += 1
            first[1] = s
        else:
            flag = 'second'
    if flag == 'second':
        if second[1] == 'sign':
            second[0] += 1
            second[1] = s
        elif s == second[1]:
            second[0] += 1
        elif s == '0':
            continue
        else:
            flag = 'third'
    if flag == 'third':
        if third[1] == 'sign':
            third[0] += 1
            third[1] = s
        elif s == third[1]:
            third[0] += 1

print(first, second, third)
print(sign)


result = 0

if second[0] >= 2 :
    result = -1
elif second[0] == 0 :
    result = 0
elif third[0] == 0:
    result = first[0]
elif first[0] == "+" and nums[-1] <= nums[0]:
    result = first[0]
elif first[0] == "-" and nums[-1] >= nums[0]:
    result = first[0]
else:
    result = -1

print(result)

'''
5
3 0 1 1 1

'''