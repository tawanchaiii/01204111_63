n = int(input("n: "))
A = [[False]*n for _ in range(n)]
x = int((n-1) /2 )
for i in range(n):
    A[i][i] = True
    A[i][n-1-i] = True
    A[i][x] = True
    A[x][i] = True
for i in range(n):
    for j in range(n):
        if A[i][j] == True : print("+",end='')
        else : print(" ",end='')
    print()