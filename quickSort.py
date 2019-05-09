def partition(arr,p_start,p_end):
    pivot = arr[p_end]
    pIndex = p_start
    
    for i in range(p_start,p_end):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex=pIndex+1
            
    arr[pIndex],arr[p_end] = arr[p_end],arr[pIndex]
    return pIndex
    
def quickSort(arr,start,end):
    if start < end:
        partIndex = partition(arr,start,end)
        quickSort(arr,start, partIndex-1)
        quickSort(arr, partIndex+1,end)

A = [7,2,100,6,8,5,3,4]
n = len(A)
quickSort(A,0,n-1)
print(A)