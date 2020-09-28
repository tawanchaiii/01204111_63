def findElement(rna,want):
    ans = []
    jum = []
    for i in range(len(rna)-len(want)+1):
        check = True
        cc = False
        for j in range(len(want)):
            if i in jum:
                cc = True
                check = False
                break
            elif want[j] != rna[i+j] :
                check = False
                break
        if check :
            ans.append(i)
            for k in range(i,i+len(rna)):
                jum.append(k)
    return ans




dna = input("DNA: ")
rna = ''
first = "AUG"
one = "UAA"
two = "UGA"
three = "UAG"
for i in range(len(dna)):
    if dna[i] == 'A':
        rna += 'U'
    elif dna[i] == 'C':
        rna += 'G'
    elif dna[i] == 'G':
        rna += 'C'
    elif dna[i] == 'T':
        rna += 'A'
    
f = findElement(rna,first)
ee = []
ee.append(findElement(rna,one))
ee.append(findElement(rna,two))
ee.append(findElement(rna,three))
ans = []
for i in range(3):
    for j in range(len(ee[i])):
        if (ee[i][j]-f[0]) % 3 == 0:
            ans.append((ee[i][j]-f[0]) // 3)
            break
q = min(ans)
print(f'{q} Amino acid(s)')