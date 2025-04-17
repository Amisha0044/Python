r1 = int(input("Enter no. of rows in matrix-1: "))
c1 = int(input("Enter no. of columns in matrix-1: "))
r2 = int(input("Enter no. of rows in matrix-2: "))
c2 = int(input("Enter no. of columns in matrix-2: "))

if c1!=r2:
    print("multiplication is not possible")
else:
    mat1=[]
    for i in range(r1):
        row_lt = []
        for j in range(c1):
            b = int(input("Enter elements of matrix-1, separated by enter:"))
            row_lt.append(b)
        mat1.append(row_lt)
    print(mat1)     # [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    mat2=[]
    for i in range(r2):
        row_lt = []
        for j in range(c2):
            b = int(input("Enter elements of matrix-2, separated by enter:"))
            row_lt.append(b)
        mat2.append(row_lt)
    print(mat2)     # [[1, 3, 5], [5, 7, 9], [5, 6, 7]]

    print("......")
    mul=[]
    for i in range(r1):
        row_lt = []
        for j in range(c2):
            sum=0
            for k in range(c1):
                sum = sum + mat1[i][k]*mat2[k][j]
            row_lt.append(sum)
        mul.append(row_lt)

    print(".....")
    print(mul)      # [[260, 350, 440], [590, 830, 1070], [920, 1310, 1700]]
    for i in range(r1):
        for j in range(c2):
            print(mul[i][j], end='  ')
        print()
    # 260    350    440
    # 590    830    1070
    # 920    1310   1700