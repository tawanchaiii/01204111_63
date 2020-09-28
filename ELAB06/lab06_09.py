A = []
for i in range(3):
    b = list(map(int,input(f'Row {i+1} : ').split()))
    A.append(b)
    A[i].append(A[i][0])
    A[i].append(A[i][1])

a = 0
b = 0 

for i in range (2,-1,-1) :
    x = 1 
    for j in range(3):
        x *= A[j][i+j]
    a += x 
for i in range (4,1,-1) :
    x = 1 
    for j in range(3):
        x *= A[j][i-j]
    b += x 
print(a-b)