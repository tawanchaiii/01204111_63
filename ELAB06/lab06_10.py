text = input("Text: ")
sub = input("Substring: ")
ans = ''
jum = []

for i in range(len(text)-len(sub)+1):
    check = True
    cc = False
    for j in range(len(sub)):
        if i in jum:
            cc = True
            check = False
            break
        elif sub[j] != text[i+j] :
            check = False
            break
        
    if check :
        ans = ans + '[' + text[i:i+len(sub)] +']'
        for k in range(i,i+len(sub)):
            jum.append(k)
    elif cc :
        pass
    else :
        ans += text[i]
if ans[len(ans)-1] != ']' :
    ans+= text[len(text)-len(sub)+1:]
if ans == text:
    print("Not found")
else :
    print(ans)
