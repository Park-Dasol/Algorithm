import re
def check(source):
    global ans
    A = ''.join(re.split('100+1+',source))
    print(A)
    if not len(A):
        ans = 'YES'
        return
    if len(A) >= 4 and A != source:
        check(A)
    B = ''.join(re.split('01',source))
    print('split', re.split('01',source))
    print(B)
    if not len(B):
        print('B')
        ans = 'YES'
        return
    if len(B) >= 2 and B !=source:
        check(B)







N =int(input())
# pattern = (100+1+ | 01)+


for i in range(N):
    ans = 'NO'
    source = str(input())
    check(source)
    print(ans)


