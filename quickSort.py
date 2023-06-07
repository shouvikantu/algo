def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high):
       if arr[j] <= pivot:
           i = i+1
           arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

data = [4,3,5,2,1,9,3,12,4]

size = len(data)

print(quickSort(data, 0, size - 1))
