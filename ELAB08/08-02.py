def func(file):
    data = file.read()
    a = data.split('\n')
    lis = [i.split(' ') for i in a]
    b1 = []
    for i in range(len(data)):
        if data[i] == '.' and i != len(data)-1:
            if ord(data[i+1]) >= 48 and ord(data[i+1]) <= 57 and ord(data[i-1]) >= 48 and ord(data[i-1]) <= 57:
                pass
            else:
                b1.append(0)
        if data[i] == '.' and i == len(data)-1 :
            b1.append(0)
    return b1,a,lis
        
name = input("File name: ")
file = open(name, "r")
b,a,lis = func(file) 
s = 0
for i in range(len(lis)) :
	s = len(lis[i])
print(f"There are {len(b)} sentences and {s} words.")

