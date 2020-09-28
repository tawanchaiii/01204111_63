import math
l = [0,0,0,0,0]
l[0] = int(input("Input a: "))
l[1] = int(input("Input b: "))
l[2] = int(input("Input c: "))
l[3] = int(input("Input d: "))
l[4] = int(input("Input e: "))
mean = float((l[0]+l[1]+l[2]+l[3]+l[4])/5)
print(f"mean: {mean:.3f}")
sum = 0
for i in range(5):
	sum +=(l[i]-mean)*(l[i]-mean)
want = float(math.sqrt(sum/5))
print(f"sd: {want:.3f}")