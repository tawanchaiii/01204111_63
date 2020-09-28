want = int(input("Distance from starting point(m.): "))
c = 0
now = 0
if(want == 0):
	print("0")
while True:
	
	if now<want :
		now+=5
		print(f"{now}",end=' ')
		now-=2
		print(f"{now}",end=' ')
		c = c+1
	elif now > want:
		now-=4
		print(f"{now}",end=' ')
		now+=3 
		print(f"{now}",end=' ')
		c = c+1
	else:
		break
if(want!=0):
	print(f"\nBuzz moved {c} set(s)")
else:
	print(f"Buzz moved {c} set(s)")
