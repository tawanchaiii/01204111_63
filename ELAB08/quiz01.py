#print([(2*i-1)*'*' for i in range(1,6)])

def plus(A,B):
     return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A)) ]
def transpose(A):
     return [[A[j][i] for j in range(len(A))] for i in range(len(A[0])) ]
#print(plus([[1,2],[3,4]],[[5,6],[7,8]]))
print(transpose([[1,2],[3,4]]))