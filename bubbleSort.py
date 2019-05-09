A = [2,100,4,1,5,3]

for i in range(1, len(A)): #runtime: (n-1)
   for j in range(0, len(A)-1): #runtime: (n-1)
        if A[j+1]< A[j]:        #runtime: c
            A[j], A[j+1] = A[j+1], A[j]
            print(A)
print(A)

#T(n)=(n-1)*(n-1)*c
#    =cn^2 - 2cn + 1 ~n^2 

# O(n^2)