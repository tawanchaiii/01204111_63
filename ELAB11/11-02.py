import csv
def fu(name):   
    with open(name) as file:
        reader = csv.reader(file)
        next(reader)
        A = list()
        for row in reader : 
            A.append(float(row[4]))
        print(f"Minimum: {min(A):.2f}")
        print(f"Maximum: {max(A):.2f}")
        print(f"Average temperature: {sum(A) / len(A):.4f}")
name = input("Enter file name: ")
fu(name)