def printans(res) :
	for i in range(len(res)):
	    for j in range(len(res[0])):
	        print(f"{res[i][j]:^5}",end=" ")
	    print()

def openfile_save(file) :
	f = open(file)
	r = f.readlines()
	lis = [ i.strip().split(' ') for i in r if i!=[] ]
	return lis

def minus_matrix(A,B) :
	return [  [A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

def plus_matrix(A,B) :
	return [  [A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

def mul_matrix(A,B) :
	return [ [ sum( A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A)) ]

def chnow(now,checknow,start,i,comm) :
	if checknow == 0 :
		now = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(start,i)  ]
	end = len(lis)
	for j in range(i+1,len(lis)) :
		if lis[j][0] in comm :
			end = j
			break
	B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
	return now,B

def check(lis) :
	start = 0
	checknow = 0
	now = []
	comm = ['+','-','*']
	#print(lis)
	for i in range(len(lis)) :
		if lis[i][0] == '*' :
			A,B = chnow(now,checknow,start,i,comm)
			now = mul_matrix(A,B)
			checknow = 1

		if lis[i][0] == '+' :
			A,B = chnow(now,checknow,start,i,comm)
			now = plus_matrix(A,B)
			checknow = 1

		if lis[i][0] == '-' :
			A,B = chnow(now,checknow,start,i,comm)
			now = minus_matrix(A,B)
			checknow = 1
	return now


file = input('File name: ')
lis = openfile_save(file)
printans(check(lis))
