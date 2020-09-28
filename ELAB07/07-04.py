x = input("Text: ")
text = x 
sub = input("Substring: ")
jum = []
x = x.replace(sub,'['+sub+']')
if text != x:
    print(x)
else :
    ans = ''
    for i in range(len(text)-len(sub)+1):
        check = True
        cc = False
        cnt = 0 
        indexx = 0 
        for j in range(len(sub)):
            if i in jum:
                cc = True
                check = False
                break
            elif sub[j] != text[i+j] :
                indexx = j + i
            else :
                cnt+=1
        if check and cnt == len(sub)-1:
            r = len(text[i:indexx])
            ans = ans + '[' + text[i:indexx] + '?' + text[indexx+1:i+len(sub)] +']'
            for k in range(i,i+len(sub)):
                jum.append(k)
        elif cc :
            pass
        else :
            ans += text[i]
   
    if ans[len(ans)-1] == ']' :
        x = int(jum[len(jum)-1])
        ans+= text[x+1:]
    if ans == text:
        print("Not found")
    else :
        print(ans)
