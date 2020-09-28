x = int(input())

l = [1000,500,100,50,20,10,5,1]

for i in range(8):
	print(f"{l[i]} => {x//l[i]}")
	x = x%l[i]