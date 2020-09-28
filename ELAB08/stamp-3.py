
'''
#01
def openfile_save(file) :
	with open(file) as f :
		s = f.readlines()
		lists = [ i.strip().split(' ') for i in s if i.strip()!='' ]
	return lists

def findmaxandprint(std) :
	maxx = 0
	summ = [0]*len(std)
	for i in range(len(std)) :
		maxc = int(-1) 
		minc = 1e9
		for j in range(1,len(std[i])) :
			summ[i] = summ[i] + int(std[i][j])
			maxc = max(int(std[i][j]),maxc)
			minc = min(int(std[i][j]),minc)
		maxx = max(summ[i]-maxc-minc,maxx)
		summ[i] = summ[i]-maxc-minc
	print(maxx)
	for i in range(len(std)) :
		if summ[i] == maxx :
			print(std[i][0])


file = input('File name: ')
std = openfile_save(file) 
#print(std)
findmaxandprint(std)
'''


'''
#02
def openfile_save(file) :
	with open(file,encoding='utf-8') as f :
		a = f.read().split('\n')
		#print(a)
	lis = [ i.split(' ')   for i in a ]
	#print(lis)
	with open(file,encoding='utf-8') as f :
		b1 = []
		b = f.read()
		for i in range(len(b)) :
				if b[i] == '.' and i != len(b)-1 :
					#print(ord(b[i+1]))
					if ord(b[i+1]) >= 48 and  ord(b[i+1])<= 57 and ord(b[i-1]) >= 48 and  ord(b[i-1])<= 57 :
						pass
					else :
						b1.append(0)
				if b[i] == '.' and i == len(b)-1 :
					b1.append(0)
		#print(b1)
	return b1,a,lis


file = input('File name: ')
b,a,lis = openfile_save(file) 


summ = 0
for i in range(len(lis)) :
	summ = len(lis[i])
print("There are %d sentences and %d words."%(len(b),summ))
'''

'''
#03
def openfile_save(file) :
	f = open(file)
	r = f.readlines()
	lis = [ i.strip().split(',') for i in r ]
	return lis
	

def enter_number(lis,n):
	l = len(lis)
	if n == 1 :
		print(l)
	
	elif n == 2 :
		maxx = 0
		summ = [0]*len(lis[0])

		for i in range( len(lis[0])-1 ):
			for j in range(1,l) :
				summ[i] = summ[i] + int(lis[j][i])
			maxx = max(maxx,summ[i])
		for i in range( len(lis[0]) ):
			if summ[i] == maxx :
				#print(maxx)
				print(lis[0][i])

	elif n == 3 :
		for i in range( len(lis[0])-1 ):
			blue = []
			if lis[0][i] == 'blueplanet' :
				for j in range(1,l) :
					blue.append(int(lis[j][i]))
				blue.sort(reverse=True)
				for j in range(3) :
					print(blue[j],end=' ')
				print()


	elif n == 4 :
		maxx = 0
		summ = [0]*l

		for i in range( 1,l ):
			for j in range(len(lis[0])-1) :
				summ[i] = summ[i] + int(lis[i][j])
			maxx = max(maxx,summ[i])

		for i in range( l ):
			if summ[i] == maxx :
				#print(maxx)
				print(lis[i][len(lis[0])-1],maxx)


	elif n == 5 :
		for i in range( len(lis[0])-1 ):
			tvshow = []
			if lis[0][i] == 'tvshow' :
				for j in range(1,l) :
					tvshow.append(int(lis[j][i]))
				tvshow.sort(reverse=True)
				for j in range(1,l) :
					if int(lis[j][i]) == tvshow[0] :
						print(lis[j][len(lis[0])-1],tvshow[0])


	elif n == 6 :
		countt = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'korea' :
				for j in range(1,l) :
					if int(lis[j][i]) > 500 :
						countt = countt + 1
		print(countt)

	elif n == 7 :
		savesiam = 0
		savefood = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'siam' :
				savesiam = i
			if lis[0][i] == 'food' :
				savefood = i
		countt = 0
		#print(savesiam,savefood,l)
		for i in range( 1, l ):
			if int(lis[i][savesiam]) > int(lis[i][savefood]) :
				countt = countt + 1
		print(countt)

	elif n == 8 :
		maxx = 0
		summ = [0]*l
		a = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'rajdumnern' :
				a  = i

		for i in range( 1,l ):
			for j in range(len(lis[0])-1) :
				summ[i] = summ[i] + int(lis[i][j])
			maxx = max(maxx,int(lis[i][a])/summ[i])
		for i in range( 1,l ):
			if int(lis[i][a])/summ[i] == maxx :
				#print(maxx)
				print(lis[i][len(lis[0])-1])


	elif n == 9 :
		maxx = 0
		summ = [0]*l
		countt = 0
		for i in range( 1,l ):
			check = []
			for j in range(len(lis[0])-1) :
				summ[i] = summ[i] + int(lis[i][j])
				check.append(int(lis[i][j]))
			check.sort(reverse=True)
			if (check[0]+check[1])/summ[i] >= 0.7 :
				countt = countt + 1
		print(countt)
		

	elif n == 10 :
		countt = 0
		a = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'pantip' :
				a  = i

		for i in range( 1,l ):
			if int(lis[i][a]) == 0 :
				countt = countt + 1
		print(countt)

file = input('File name: ')
lis = openfile_save(file)
enter_number( lis , int( input('enter number: ') ) ) 
'''

'''
#04
def printans(res) :
	for i in range(len(res)):
	    for j in range(len(res[0])):
	        print(f"{res[i][j]:^5}",end=" ")
	    print()

def openfile_save(file) :
	f = open(file)
	r = f.readlines()
	lis = [ i.strip().split(' ') for i in r ]
	return lis

def minus_matrix(A,B) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] - B[i][j]
	return ans

def plus_matrix(A,B) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] + B[i][j]
	return ans

def mul_matrix(A,B) :
	x1 = len(A)
	x2 = len(A[0])
	y1 = len(B)
	y2 = len(B[0])
	ans = [ [0]*y2 for i in range(x1) ]
	for i in range(0,x1) :
		for j in range(0,y2) :
				for l in range(0,y1) :
					ans[i][j] += A[i][l]*B[l][j]
	return ans



def check(lis) :
	start = 0
	checknow = 0
	now = []
	comm = ['+','-','*']
	#print(lis)
	for i in range(len(lis)) :
		if lis[i][0] == '*' :
			if checknow == 0 :
				A = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(start,i)  ]
				end = len(lis)
				for j in range(i+1,len(lis)) :
					if lis[j][0] in comm :
						end = j
						break
				B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
				now = mul_matrix(A,B)
				#printans(now)
				#print(now,B)
				checknow = 1
			else :
				end = len(lis)
				for j in range(i+1,len(lis)) :
					if lis[j][0] in comm :
						end = j
						break
				B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
				now = mul_matrix(now,B)
				#print(now)
				#printans(now)

		if lis[i][0] == '+' :
			if checknow == 0 :
				A = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(start,i)  ]
				end = len(lis)
				for j in range(i+1,len(lis)) :
					if lis[j][0] in comm :
						end = j
						break
				B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
				now = plus_matrix(A,B)
				#printans(now)
				#print(now,B)
				checknow = 1
			else :
				end = len(lis)
				for j in range(i+1,len(lis)) :
					if lis[j][0] in comm :
						end = j
						break
				B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
				#print(now,B)
				now = plus_matrix(now,B)
				#printans(now)

		if lis[i][0] == '-' :
			if checknow == 0 :
				A = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(start,i)  ]
				end = len(lis)
				for j in range(i+1,len(lis)) :
					if lis[j][0] in comm :
						end = j
						break
				B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
				now = minus_matrix(A,B)
				#printans(now)
				#print(now,B)
				checknow = 1
			else :
				end = len(lis)
				for j in range(i+1,len(lis)) :
					if lis[j][0] in comm :
						end = j
						break
				B = [  [ int(lis[xx][yy])  for yy in range(len(lis[xx]))  ]    for xx in range(i+1,end)  ]
				#print(now,B)
				now = minus_matrix(now,B)
				#printans(now)
	return now


file = input('File name: ')
lis = openfile_save(file)
printans(check(lis))

'''


#03 NEW
def readPantip(filename):
  with open(filename) as f:
    s = f.readlines()
    pt = [i.strip() for i in s]
    head = [i for i in pt[0].split(',')]
    room, uid = [], []
    for i in range(1, len(pt)):
      line = pt[i].split(',')
      len_line = len(line)
      uid.append(line[len_line-1])
      tmp = [int(line[i]) for i in range(len_line-1)]
      room.append(tmp)
  return head, uid, room 

def q1(m):
  print(len(m) + 1)

def q2(room, header):
  mymax, c = -99999999, 0
  row, col = len(room), len(room[0])
  for j in range(col):
    mysum = 0
    for i in range(row):
      mysum += room[i][j]
    if mysum > mymax:
      mymax = mysum
      c = j
  print(header[c])

def q3(room, header, r='blueplanet'):
  j = header.index(r)
  row = len(room)
  blue = [room[i][j] for i in range(row)]
  blue.sort(reverse = True)
  for i in range(3):
    print(f'{blue[i]} ', end='')
  print()

def q4(room, header, uid):
  mymax, c = -99999999, 0
  row, col = len(room), len(room[0])
  for i in range(row):
    mysum = 0
    for j in range(col):
      mysum += room[i][j]
    if mysum > mymax:
      mymax = mysum
      c = i
  print(uid[c], mymax)

def q5(room, header, uid, r='tvshow'):
  j = header.index(r)
  mymax, c = -99999999, 0
  row = len(room)
  for i in range(row):
    if room[i][j] > mymax:
      mymax = room[i][j]
      c = i
  print(uid[c], mymax)

def q6(room, header, r='korea', top=500):
  j = header.index(r)
  row, nbUser = len(room), 0
  for i in range(row):
    if room[i][j] > top:
      nbUser += 1
  print(nbUser)

def q7(room, header, r1='siam', r2='food'):
  j1 = header.index(r1)
  j2 = header.index(r2)
  row, nbUser = len(room), 0
  for i in range(row):
    if room[i][j1] > room[i][j2]:
      nbUser += 1
  print(nbUser)

def q8(room, header, uid, r='rajdumnern'):
  j1 = header.index(r)
  row, col = len(room), len(room[0])
  tmp = []
  for i in range(row):
    mysum = sum(room[i])
    tmp.append(room[i][j1]*100/mysum)
  mymax = max(tmp)
  print(uid[tmp.index(mymax)])

def q9(room, per=70):
  row, col = len(room), len(room[0])
  nbUser = 0
  for i in range(row):
    PER = sum(room[i]) * per / 100
    j = 0
    while j < col:
      k = j+1
      while k < col:
        if room[i][j]+room[i][k] > PER:
          nbUser += 1
          k, j = col, col
        k += 1
      j += 1
  print(nbUser)

def q10(room, header, r='pantip'):
  j1 = header.index(r)
  row, col = len(room), len(room[0])
  nbUser = 0
  for i in range(row):
    if room[i][j1] == 0:
      nbUser += 1
  print(nbUser)

### Main begins from here
fn = input('File name: ')
header, uid, room = readPantip(fn)

while True :
	q = int(input('enter number: '))
	if q==1:
	   q1(room)
	elif q==2:
	   q2(room, header)
	elif q==3:
	   q3(room, header, 'blueplanet')
	elif q==4:
	   q4(room, header, uid)
	elif q==5:
	   q5(room, header, uid, 'tvshow')
	elif q==6:
	   q6(room, header, 'korea', 500)
	elif q==7:
	   q7(room, header, 'siam', 'food')
	elif q==8:
	   q8(room, header, uid, 'rajdumnern')
	elif q==9:
	   q9(room, 70)
	elif q==10:
	   q10(room, header, 'pantip')
