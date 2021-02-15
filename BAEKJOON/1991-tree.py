def travle(K,dir):
    if dir == 'pre':
        print(K, end="")
        if tree[K][0] != '.':
            travle(tree[K][0], 'pre')
        if tree[K][1] != '.':
            travle(tree[K][1], 'pre')
    elif dir == 'in':
        if tree[K][0] != '.':
            travle(tree[K][0], 'in')
        print(K, end="")
        if tree[K][1] != '.':
            travle(tree[K][1], 'in')
    else:
        if tree[K][0] != '.':
            travle(tree[K][0], 'post')
        if tree[K][1] != '.':
            travle(tree[K][1], 'post')
        print(K, end="")


N = int(input())
tree = dict()
for i in range(N):
    p, f, s = map(str, input().split())
    tree[p] = [f, s]
travle('A', 'pre')
print()
travle('A', 'in')
print()
travle('A', 'post')


