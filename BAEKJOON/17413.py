def get_sorted():
    flag = False
    tagged = False
    for i in range(len(words)):
        if words[i] == '<':
            tagged = True
        if words[i] == '>':
            tagged = False
        if flag == False and words[i].isalnum() == True:
            if tagged == False:
                flag = True
                s = i
        if flag == True and (i == len(words) - 1 or words[i + 1].isalnum() == False):
            flag = False
            e = i
            get_swapped(s, e)


def get_swapped(s, e):
    while s < e:
        words[s], words[e] = words[e], words[s]
        s += 1
        e -= 1



words = list(input())

get_sorted()
res = ''.join(words)
print(res)

