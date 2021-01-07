import sys
words =list(map(str, sys.stdin.readline().rstrip()))
cnt = 0
i = len(words) -1
while i >= 0 :
    cnt += 1
    if words[i] == '=':
        if i - 2 >= 0 and words[i-1] == 'z' and words[i-2] =='d':
            i -= 3
        elif i -1 >= 0 and (words[i-1] in ['c', 's', 'z']):
            i -= 2
    elif words[i] == 'j':
        if i -1 >= 0 and (words[i-1] in ['l', 'n']):
            i -= 2
        else:
            i -= 1

    elif words[i] == '-':
        if i -1 >= 0 and (words[i-1] in ['c', 'd']):
            i -= 2
        else:
            i -= 1
    else:
        i -= 1

print(cnt)