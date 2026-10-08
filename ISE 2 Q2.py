A = [
    [1,2,3,]
    [4,5,6,]
    [7,8,9,]
 ]
B = [
    [1,2,3,]
    [4,5,6,]
    [7,8,9,]
 ]
addition=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append (A[i][j]+B[i][j])
        addition.append(row)
subtraction=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append (A[i][j]-B[i][j])
        subtraction.append(row)

print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

print("\nMatrix Addition(A+B):")
for row in addition:
    print(row)
    
print("\nMatrix Subtraction(A-B):")
for row in subtraction:
    print(row)
        
