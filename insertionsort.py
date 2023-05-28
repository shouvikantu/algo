def insertionSort(Arr, Visual, timeT):
    for i in range(1,len(Arr)):
        key = Arr[i]
        j= i-1
        while j >=0 and Arr[j]>key:
            Arr[j+1], Arr[j] = Arr[j], Arr[j+1]
            j=j-1
        Visual(Arr, )

print(insertionSort([4,3,5,2,1,9,3,12,4]))