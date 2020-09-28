def mul_const(A,c) :
    n = len(A) 
    m = len(A[0]) 
    arr = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(0)
        arr.append(b) 
    for i in range(n):
        for j in range(m):
            arr[i][j] = A[i][j]*c
    return arr
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

A = [[1,2],[3,4],[5,6]]
c = 2

arr = mul_const(A,c)
print_matrix(arr)