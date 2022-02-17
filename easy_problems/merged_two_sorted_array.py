"""
Python program to merge two sorted array. I have to improve this solution when finding duplecate entry
"""

def merge_two_sorted_arrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1+n2)
    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k+=1
            i+=1

        else:
            arr3[k] = arr2[j]
            k+=1
            j+=1

    while i < n1 :
        arr3[k] = arr1[i]
        k+=1
        i+=1

    while j < n2 :
        arr3[k] = arr2[j]
        k+=1
        j+=1

    print(arr3)

arr1 = [1,2,3,4,8]
arr2 = [2,4,5,6,7]
n1 = len(arr1)
n2 = len(arr2)

merge_two_sorted_arrays(arr1,arr2,n1,n2)
