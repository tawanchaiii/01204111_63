def chartoint (num):
    arr = []
    for i in num :
        arr.append(int(i))
    return arr 
def mintomax(num):
    arr = num.copy()
    l = len(arr)
    for i in range(l-1) :
        for j in range(i+1,l) :
            if arr[j] < arr[i] :
                temp = arr[i] 
                arr[i] = arr[j]
                arr[j] = temp
    return arr
def cut(num):
    arr = []
    for i in num :
        if not i in arr:
            arr.append(i)
    return arr

num = input().split()
num = chartoint(num)
num = mintomax(num)
num = cut(num)

for i in range (0,len(num),1):

  print(num[i],end=' ')