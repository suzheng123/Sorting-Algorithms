def mergeSort(arr):
    n = len(arr)
    if n>1: 
        mid = n/2
        L = arr[:mid] #CANNOT WORK WITH PYTHON3
        R = arr[mid:] 

        print(L)
#       print(R)
        mergeSort(L)
        mergeSort(R)

        nl = len(L)
        nr = len(R)
    
        i=j=k=0    
        while i<nl and j<nr: 
            if L[i]<R[j]:
                arr[k]=L[i]
                i=i+1
            else: 
                arr[k]=R[j]
                j=j+1
            k=k+1
        while i<nl:
            arr[k]=L[i]
            i=i+1
            k=k+1
        while j<nr:
            arr[k]=R[j]
            j=j+1
            k=k+1
            
A = [2,100,4,1,5,3,7,90]    
mergeSort(A)
print(A)
'''
#copied, can work with python3
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
'''