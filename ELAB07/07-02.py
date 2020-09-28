x,y = input("Grid Size: ").split()
x = int(x)
y = int(y)
n = int(input("Number of mine(s): "))
A = [[0] * x for _ in range(y)]
for i in range(n):
    a,b = input(f"Mine#{i+1}: ").split()
    a = int(a)
    b = int(b)
    A[b][a] = -1
    for j in range(-1,2):
        for k in range(-1,2):
            q = b+j
            w = a+k
            if q == 0 and w == 0 :
                pass
            elif q < 0 or q >= y or w <0 or w >=x :
                pass
            elif  A[q][w] == -1 :
                pass
            else :
                A[q][w]+=1

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == -1 :
            print("X ",end='')
        else :
            print(f"{A[i][j]} ",end='')
    
    print()