import math
def fac(n) :
  if n == 0 :
    return 1
  else : 
    return n * fac(n-1)
d = float(input("degree: "))
dg = d
d = d*math.pi/180
sin = 0.0
cos = 0.0
for i in range(0,11) :
  cos+= (((-1)**i ) * d**(2*i)) / (fac(2*i))
for i in range(1,11) :
  sin+= ((-1)**(i-1) * d**(2*i-1)) / (fac(2*i-1))
print(f"sin({dg:.2f}): {sin:.10f}")
print(f"cos({dg:.2f}): {cos:.10f}")