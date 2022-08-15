rows = int(input("Enter no.of rows: "))
columns = int(input("Enter no.of columns: "))

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows-1:
            print("*\t", end="")
        elif j == 0 or j == columns-1:
            print("*\t", end="")
        elif j != 0 or j != columns - 1:
            if j != 0 or j != columns-1:
                print("\t", end='')

    print("\n")
