import math as mt

def ternarySearch(l,r,key, arr):
    if (r>= l):
        mid1 = l + (r-1) //3
        mid2 = r - (r-1) //3

        if (arr[mid1] == key):
            return mid1
        if (arr[mid2]==key):
            return mid2
        if (key < arr[mid1]):
 
            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, arr)
         
        elif (key > arr[mid2]):
 
            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, arr)
         
        else:
 
            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1,
                                 mid2 - 1, key, arr)
         
    # Key not found
    return -1