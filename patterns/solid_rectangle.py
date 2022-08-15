rows = int(input("Enter no.of rows: "))
columns = int(input("Enter no.of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*\t", end=""),
    print("\n")
