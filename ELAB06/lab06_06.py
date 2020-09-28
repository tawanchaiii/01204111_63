def power_matrix(A,c) :
    cc = A.copy()
    for i in range(c-1) :
        m = len(A)
        result = [ [0]*m for i in range(m) ]
        for i in range(len(cc)):
            for j in range(len(A[0])):
                for k in range(len(A)):
                    result[i][j] +=  cc[i][k] * A[k][j] 
        cc = result.copy()
    return cc
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()


A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2

arr = power_matrix(A,c)
print_matrix(arr)