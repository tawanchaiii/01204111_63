x = int(input("Estimated time : "))

lo = x//7
want = x * 2.5
sa = 0
sb = 0
sc = 0
for i in range(lo):
	print(f"Week{i+1}")
	a = int(input("Physical therapy : "))
	b = int(input("Weight training : "))
	c = int(input("Fitness training : "))
	sa+=a
	sb+=b
	sc+=c
if(sa >= want and sb >= want and sc >= want):
	print("Buzzy has recovered in time.")
else:
	print("Buzzy has not recovered in time.")