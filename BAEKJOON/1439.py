import sys

S = sys.stdin.readline().rstrip()
lst = []
for i in range(0, len(S)):
    if i == 0:
       lst.append(S[i])
    if i>0 and S[i] != S[i-1]:
       lst.append(S[i])
print(min(lst.count('1'), lst.count('0')))



