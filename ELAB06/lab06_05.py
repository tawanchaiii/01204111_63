def mul_matrix(A,B) :
    result = list()
    m = len(A)
    n = len(B[0])
    for i in range(m):
        b = []
        for j in range(n):
            b.append(0)
        result.append(b)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j] 
    return result
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
x = mul_matrix(A,B)
print_matrix(x)