text = list(map(str,input('Text: ').split()))
chain = 0
lmaxx = -1

l = 1 
for i in range(1,len(text)):
    cnt = 0
    for k in range(len(text[0])):
        if(text[i][k] == text[i-1][k]):
            cnt+=1
    if cnt >= len(text[0])-2:
        l+=1
    if cnt < len(text[0])-2 or i==len(text)-1:
        if cnt < len(text[0])-2 and i==len(text)-1:
            chain+=1
        chain+=1
        if l > lmaxx:
            lmaxx = l
        l = 1
    
    
               
        
print(f"{chain} Chain(s). Maximum length is {lmaxx} word(s).")
#HEAD HEAP LEAP TEAR REAR BAER BAET BEEP JEEP JOIP JEIP AEIO