comm = ['+', '-', '*']


def printans(res):
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}", end=" ")
        print()


def openfile_save(file):
    f = open(file)
    r = f.readlines()
    lis = [i.strip().split(' ') for i in r]
    return lis


def minus_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def plus_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mul_matrix(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]


def setNow(lis):
    i = 0
    while True:
        if lis[i][0] == '+' or lis[i][0] == '-' or lis[i][0] == '*':
            return [[int(lis[xx][yy]) for yy in range(len(lis[xx]))] for xx in range(0, i)], i
        i += 1


def setB(lis, start):
    end = len(lis)
    for j in range(start+1, end):
        if lis[j][0] in comm:
            end = j
            break
    return [[int(lis[xx][yy]) for yy in range(len(lis[xx]))] for xx in range(start+1, end)]


def check(lis, s, n):
    start = 0
    end = len(lis)
    now = n.copy()
    for i in range(s, len(lis)):
        if lis[i][0] == '*':
            B = setB(lis, i)
            now = mul_matrix(now, B)
        if lis[i][0] == '+':
            B = setB(lis, i)
            now = plus_matrix(now, B)
        if lis[i][0] == '-':
            B = setB(lis, i)
            now = minus_matrix(now, B)
    return now


file = input('File name: ')
lis = openfile_save(file)
now, start = setNow(lis)
printans(check(lis, start, now))
