d = int(input("Day: "))
a0 = 1 
a1 = 1
if (d==1):
	print(f"{a0}",end=" ")
elif (d==2):
	print(f"{a0} {a1}",end=" ")
else:
	print(f"{a0} {a1}",end=" ")
	for i in range(d-2):
		a2 = a0+a1
		print(f"{a2}",end=" ")
		a0 = a1
		a1 = a2