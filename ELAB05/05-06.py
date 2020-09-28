def draw(arr):
    for i in range(len(arr)) :
        for j in range(i+1) :
            print(f"{arr[i]}",end="")
        print("\n",end="")

while True:
    arr = input().split()
    if len(arr) == 1 and arr[0] == '0' :
        print("Good Bye.")
        break
    draw(arr)
