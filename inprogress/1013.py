import re
def check(source):
    global ans
    A = re.split('100+1+', source)
    for a in A:
        if len(a) and a != source:
            check(a)
    B = re.split('01', source)
    for b in B :
        if len(b) and b != source:
            check(b)
    if len(B) == 0 or len(A) == 0:
        ans = 'YES'
    print(A)
    print(B)



N =int(input())
# pattern = (100+1+ | 01)+
for i in range(N):
    ans = 'NO'
    source = str(input())
    check(source)
    print('-------------')

    print(ans)


