n = int(input())
x = 2*n-1
A = [[0]*x for _ in range(x)] 
c = n
for k in range(n):
    for i in range(k,x-k):
        for j in range(k,x-k):
            A[i][j] = c
    c-=1

for i in range(x):
    for j in range(x):
        print(f"{A[i][j]}",end= " ")
    print()