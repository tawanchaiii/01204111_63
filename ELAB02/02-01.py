minute = int(input("How long have Buzz played ?: "))
h = minute//60
x = 0
if minute%60 > 20 :
	h+=1

if 2<=h<4:
	print(f"Total price is {(h*900*0.9):.0f} baht.")
elif h==4:
	print(f"Total price is {(h*900*0.8):.0f} baht.")
elif h>=5:
	print(f"Total price is {(h*900*0.7):.0f} baht.")
else:
	print(f"Total price is {(h*900):.0f} baht.")