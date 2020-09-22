students, K = map(int, input().split())
mat = [[0]*7 for _ in range(2)]
#girl : 0, boy : 1
for s in range(students):
    gender, grade = map(int, input().split())
    mat[gender][grade] +=1

result = 0
for i in range(2):
    for j in range(7):
        if mat[i][j] % K >0:
            result += mat[i][j] // K + 1
        else:
            result += mat[i][j] // K
print(result)
