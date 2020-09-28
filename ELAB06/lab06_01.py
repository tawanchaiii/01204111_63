def zero(n):
  m = []
  for i in range(n):
    b = []
    for j in range(n):
      b.append(0)
    m.append(b)
  return m  
def plus_matrix(A,B) :
    arr = zero(3)
    for i in range(3):
        for j in range(3):
            arr[i][j] = A[i][j]+B[i][j]
    return arr
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]

arr = plus_matrix(A,B)
print_matrix(arr)