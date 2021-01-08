import sys

words = list(sys.stdin.readline().rstrip())
# print(words)
result = {}
for I in range(len(words)):
    i = words[I].upper()
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

m_num = 0

for key, value in result.items():
    if value > m_num :
        m_num = value
        ans = key
    elif value == m_num:
        ans = '?'
print(ans)

