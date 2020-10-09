n = int(input())
A = [[0]*n for _ in range(n)]

down = False
c = 1 
for k in range(n-1):
    if down:
        i = n-k-1
        j = 0
        for g in range(k+1):
            A[i+g][j+g] = c
            c+=1
    else :
        i = n-1
        j = k
        for g in range(k+1):
            A[i-g][j-g] = c
            c+=1
    down = not down
for i in range(n):
    if down:
        A[i][i] = c
        c+=1
    else :
        A[n-i-1][n-i-1] = c
        c+=1
down = not down


for k in range(n-1):
    if down:
        i = 0
        j = 1+k
        for g in range(n-k-1):
            A[i+g][j+g] = c
            c+=1
    else :
        i = n-2-k
        j = n-1
        for g in range(n-k-1):
            A[i-g][j-g] = c
            c+=1
    down = not down


for i in range(n):
    for j in range(n):
        print(f'{A[i][j]:3.0f}',end=' ')
    print()