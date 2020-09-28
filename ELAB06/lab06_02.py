def minus_matrix(A,B) :
  x = len(A)
  y = len(A[0])
  arr = [ [0]*y for i in range(x) ]
  for i in range(x):
    for j in range(y):
      arr[i][j] = A[i][j]-B[i][j]
  return arr
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()



A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]

arr = minus_matrix(A,B)
print_matrix(arr)