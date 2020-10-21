##################### 0. Readfile #####################
f = open("hello.txt")
f_contents = f.read()
f_contents = f.readline()
f_contents = f.readlines() #recommended

lis = [ i.strip().split() for i in f_contents ]


##################### 1. sort dict by key or value #####################
dic = {
 'a' : 150 ,
 'c' : 55 ,
 'b' : 500 
}
xnxx = sorted( dic.values() )
print(type(xnxx))
for i in xnxx :
 print(i)

xnxx = sorted( dic,key=dic.get )
print(type(xnxx))
for i in xnxx :
 print(i,dic[i])
##################### 2. sort array of Class by key or value #####################
class Item:
 def __init__(self,key,value):
  self.key = key
  self.value = value
 def __lt__(self,rhs):
  #if self.value == rhs.value :
  # return self.key < rhs.key
  return self.value < rhs.value

A = list()
A.append(Item('A',150))
A.append(Item('C',500))
A.append(Item('X',50))
A.append(Item('B',50))

B = sorted(A)

for i in B:
 print(f'{i.key} , {i.value}')