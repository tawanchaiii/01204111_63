A = [[1,2],[3,4],[5,6]] 
def transpose_matrix(A):
    n = len(A[0]) ## 2 
    m = len(A) ###3
    
    arr = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(0)
        arr.append(b)
    for i in range(n): ### 3
        for j in range(m): ### 2
            arr[i][j] = A[j][i]
    return arr 

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

arr = transpose_matrix(A)
print_matrix(arr)