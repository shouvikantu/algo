def selectionSort(arr):
    for i in range(len(arr)):
        low = i
        for j in range(i+1, len(arr)):
            if arr[low] > arr[j]:
                low = j
        arr[i], arr[low] = arr[low], arr[i]

    return arr

print(selectionSort([4,3,5,2,1,9,3,12,4]))