a = int(input())
b = int(input())
c = int(input())

if a>=b:
	if b>=c:
		print(f"{c} {b} {a}")
	else:  #b < c 
		if a>=c:
			print(f"{b} {c} {a}")
		else:
			print(f"{b} {a} {c}")
else:
	if a>=c:
		print(f"{c} {a} {b}")
	else:  #a < c 
		if c>=b:
			print(f"{a} {b} {c}")
		else:
			print(f"{a} {c} {b}")
