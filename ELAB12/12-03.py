
A = list()
t = False
jum = 0
re = False
while True:
    x = input()
    if x == '':
        break
    if not t : 
        jum = len(x.split())
        t = not t
    else :
        if len(x.split()) != jum :
            re = True
    A.append(list(map(int,x.split())))
minn = 1e9
if re : print("Can't Buy")
else :
    for i in range(len(A)-1):
        for j in range(len(A[0])-1): 
            minn = min(minn,A[i][j]+A[i][j+1]*1.1+A[i+1][j+1]*1.1+A[i+1][j]*1.21)

    for i in range(1,len(A)):
        for j in range(len(A[0])-1): 
            minn = min(minn,A[i][j]+A[i][j+1]*1.1+A[i-1][j+1]*1.1+A[i-1][j]*1.21)
    print(f"{minn:.2f}")