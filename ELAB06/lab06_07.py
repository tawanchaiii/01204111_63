def print_matrix(A) :
	x = len(A)
	y = len(A[0])
	for i in range(0,x) :
		for j in range(0,y) :
			print(f'{A[i][j]:^6}', end = ' ')
		print()

def plus_matrix(A,B) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] + B[i][j]
	return ans

def minus_matrix(A,B) :
    x = len(A)
    y = len(A[0])
    arr = [ [0]*y for i in range(x) ]
    for i in range(x):
        for j in range(y):
            arr[i][j] = A[i][j]-B[i][j]
    return arr
def zeroMat(A):
    c = []
    for i in range(len(A)):
      row = []
      for _ in range(len(A[i])):
        row.append(0)
      c.append(row)
    return c
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

'''def mul_matrix(A,B) :
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
    return result'''
def mul_matrix(A,B) :
    x1 = len(A)
    y2 = len(B[0])
    C = [ [0]*y2 for i in range(x1) ]
    for i in range(len(A)) :    
        for k in range(len(B[0])) :
            sum = 0 
            for j in range(len(A[0])) :
                sum += A[i][j] * B[j][k]
            C[i][k] = sum
    return C

def power_matrix(A,c) :
    tmp = A.copy()
    for _ in range(c-1) :
        tmp = mul_matrix(tmp,A)
    return tmp

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

f = plus_matrix(A,transpose_matrix(B))
b = minus_matrix(power_matrix(C,c),D)

ans = mul_matrix(f,b)

print_matrix(ans)