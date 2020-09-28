
class Rectangle:
    def __init__(self,l,w):
        self.l = l; self.w = w 
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2*(self.l + self.w)
    def is_square(self):
        if self.l == self.w :return 'This rectangle is square too.'
        else :return 'This rectangle is not square.'
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a+self.b+self.c) / 2 
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** (0.5)

    def perimeter(self):
        return self.a+self.b+self.c
    def is_right_triangle(self):
        A = []
        A.append(self.a) ; A.append(self.b) ; A.append(self.c)
        A.sort()
        if (A[2] ** 2) == (A[1] ** 2 + A[0] ** 2) : return 'This triangle is right triangle too.'
        else : return 'This triangle is not right triangle.' 
class Circle:
    def __init__(self,r):
        self.r = r 
    def area(self):
        return 3.14*(self.r**2)

    def perimeter(self):
        return 2 * 3.14  * self.r


l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.') 