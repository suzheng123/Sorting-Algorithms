A = [2,100,4,1,5,3]

for i in range(1, len(A)):
    value = A[i]
    hole = i
    while hole>0 and A[hole-1]>value:
        A[hole-1], A[hole]= A[hole], A[hole-1]
        hole = hole-1
        print(A)
    A[hole] = value
print(A)