n = int(input())
A = [[False] * n for _ in range(n) ]
for i in range(n):
    A[0][i] = True
    A[i][i] = True
    A[n-1][i] = True
    A[i][0] = True
    A[i][n-1] = True
    A[n-i-1][i] = True
for i in range(n):
    for j in range(n):
        if A[i][j] :
            print(".",end='')
        else :
            print(" ",end='')
    print()