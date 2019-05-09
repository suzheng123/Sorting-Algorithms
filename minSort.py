arr = [2,7,4,1,5,3]

for i in range(0,len(arr)):
    m = arr[i]
    for j in range(i+1, len(arr)):
        if arr[j]<arr[i]:
           arr[j], arr[i] = arr[i], arr[j]
print(arr)

#new = []
#while arr:
 #   m = arr[0]
  #  for x in arr:
   #     if x < m:
    #        m = x
#    new.append(m)
 #   arr.remove(m)
#print(new)
