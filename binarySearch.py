def binarySearch(arr, l,r, x):
    while l <=r:
        mid = l - (r-1) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] <x:
            l =mid+1
        else:
            r = mid-1

    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9],1,9,5))