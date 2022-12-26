

#Taking the input for Matrix1
r = int(input("number of rows = "))
c = int (input("number of columns = "))
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        val=int(input())
        a.append(val)
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()


#Taking the input for  Matrix2
r2 = int(input("number of rows = "))
c2 = int(input("number of columns = "))
matrix2 = []
for i in range(r2):
    a2 = []
    for j in range(c2):
        val2 = int(input())
        a2.append(val2)
    matrix2.append(a2)

for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end=" ")
    print()


#upper triangle matrix
flag=1
for i in range(0,r):
    for j in range(0,i):
        if matrix[i][j]!=0:
            flag=0
if flag==1:
    print("the matrix is upper triangular matrix")
else:
    print("the matrix is not upper triangular matrix")


#summation of diagonal elements
sum=0
sum_1=0
if r!=c:
    print("matrix is not square matrix")
else:
    for i in range(r):
        for j in range(c):
            if i==j:
                sum+=matrix[i][j]
            if (i+j)==r-1:
                sum_1+=matrix[i][j]

    print("sum of principal diagonal = ",sum)
    print("sum of secondary diagonal = ",sum_1)

# transpose
# res=[[0 for i in range(r)] for j in range(c)]
x=len(matrix)
y=len(matrix[0])
trans = [[0 for i in range(y)] for j in range(x)]


for i in range(y):
    for j in range(x):
        trans[i][j] = matrix[j][i]

for i in range(y):
    for j in range(x):
        print(trans[i][j], end=" ")
    print()


#addition of two matrix
print("addition of two matrix")
result=[]
if r==r2 and c==c2:
    for i in range(0,r):
        result.append([])
        for j in range(0,c):
            result[i].append(matrix[i][j]+matrix2[i][j])

    for i in range(r):
        for j in range(c):
            print(result[i][j], end=" ")

        print()
else:
    print("the matrix cannot be added")


#multiplication of two matrix
result=[[0 for i in range(r)] for j in range(c2)]
if r2!=c:
    print("multiplication not possible")

else:
    for i in range(0, r):
        for j in range(0, c2):
            result[i][j] = 0
            for k in range(0, r2):
                result[i][j] += matrix[i][k] * matrix2[k][j]
print("multiplication of two matrices")
for r in result:
    print(r)




#saddle point
flag=0
for i in range (len(matrix)):
    min_r=matrix[i][0]
    c_ind=0
    for j in range(len(matrix[0])):
        if matrix[i][j]<min_r:
            min_r=matrix[i][j]
            c_ind=j
    max_c=matrix[0][c_ind]
    for k in range(len(matrix)):
        if matrix[k][c_ind]>max_c:
            max_c=matrix[k][c_ind]
    
    if min_r==max_c:
        print("saddel point is:",min_r)
        flag=1
if flag==0:
    print("not a saddle point")  



#magic square
if len(matrix)!=len(matrix[0]):
    print("not magic square matrix")
else:
    #check row
    check_row=[]
    
    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix)):
            sum+=matrix[i][j]
        check_row.append(sum)

    for i in range(len(matrix)):
        if check_row[i]!=check_row[0]:
            print("not square matrix")
            break



    #column
    
    for i in range(len(matrix[0])):
        sum_col=0
        for j in range(len(matrix[0])):
            sum_col+=matrix[j][i]
    # diagonal
    sum_diag = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum_diag += matrix[i][j]
    print("addition of diagonal matrix",sum_diag)
    print("addition of row", sum)
    print("addition of columns", sum_col)

    k=sum
    k1=sum_col
    k2=sum_diag
    if k==k1==k2:
        print("yes it is magic square matrix")
    else:
        print("no it is not a magic square matrix")




