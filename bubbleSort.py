def bubbleSort(arr):
    n =len(arr)
    swap = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap=True
                arr[j], arr[j+1]= arr[j+1], arr[j]
    
        if not swap:
            return arr
    return arr
        
print(bubbleSort([4,3,5,2,1,9,3,12,4]))
