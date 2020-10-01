import csv
def fu(name):   
    with open(name) as file:
        reader = csv.DictReader(file)
        dic = dict()
        for row in reader : 
            if not row['country'] in dic :
                dic[row['country']] = list()
                dic[row['country']].append(float(row['temperature']))
            else :
                dic[row['country']].append(float(row['temperature']))
        for i in dic :
            print(f"{i} {sum(dic[i]) / len(dic[i]):.2f}")
name = input("Enter file name: ")
fu(name)