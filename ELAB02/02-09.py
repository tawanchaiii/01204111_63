num = 0
tid = 0
old = -1
k=1
first = -1
while True:
	x = int(input())
	if(old == -1):
		first = x
	if(x==0): 
		break
	if(x == old):
		k+=1
	else:
		if k!=0:
			if k>tid:
				tid = k
				num = old
		k=1

	old = x
if tid!=1 :
	print(f"{tid}\n{num}")
else:
	print(f"{tid}\n{first}")