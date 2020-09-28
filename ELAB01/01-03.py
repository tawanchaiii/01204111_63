import math
x = float(input("x: "))
y = float(input("y: "))
r = (x*x+y*y-1)**3-x*x*y*y*y
print("Result is {:.2f}".format(round(r, 2)))