sign = ["+","*","-"]
def readMatrix(file):
    r = open(file)
    f = r.readlines()
    lis = [i.strip().split() for i in f]
    return lis
def printMatrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])): 
            print(f"{A[i][j]:^5}",end = ' ')
        print()
def minus_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def plus_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mul_matrix(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
def setA(A):
    i = 0
    while True:
        if A[i][0] in sign : return [[int(A[ii][jj]) for jj in range(len(A[ii]))] for ii in range(0,i)],i
        i+=1
def setB(lis,start):
    s = start 
    end = len(lis)
    for i in range(s+1,end):
         if lis[i][0] in sign :
             end = i 
             break
    return [ [ int(lis[ii][jj]) for jj in range(len(lis[ii]))] for ii in range(s+1,end)]
def cal(lis,start,now):
    A = now.copy()
    for i in range(start , len(lis)):
        if lis[i][0] == '+' : 
            B = setB(lis,i)
            A = plus_matrix(A,B)
        elif lis[i][0] == '-' :
            B = setB(lis,i)
            A = minus_matrix(A,B)
        elif lis[i][0] == '*' :
            B = setB(lis,i)
            A = mul_matrix(A,B)
    return A


file = input("Input file name : ")
r = readMatrix(file)
A,start = setA(r)
ans = cal(r,start,A)
printMatrix(ans)