import random

# Returns index of x in list if present, else -1 (recursive binary search)
def binary_search_rec(target,list,min=None,max=None,count = None):
    if count is None:
        count = 0
    if min is None:
        min = 0
    if max is None:
        max = len(list) - 1

    mid = (max + min) // 2
    count += 1
    print(max, mid, min)

    # Check base case
    if max >= min:
        # If element is smaller than mid, then it can only
        # be present in left subarray
        if target > list[mid]:
            return binary_search_rec(target,list,mid + 1,max,count)

        # Else the element can only be present in right subarray
        elif target < list[mid]:
            return binary_search_rec(target,list,min,mid - 1,count)

        # If element is present at the middle itself
        elif target == list[mid]:
            return mid

    # If we reach here, then the element was not present
    else:
        return -1
    
# Returns index of x in list if present, else -1 (iterative binary search)
def binary_search(target,list):
    count = 0
    min = 0
    max = len(list) - 1
    mid = 0

    while min <= max:
        count += 1
        mid = (max + min) // 2
        print(max, mid, min)

        # If target is greater, ignore left half
        if target > list[mid]:
            min = mid + 1
        # If target is smaller, ignore right half
        elif target < list[mid]:
            max = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

#Test list
list = [16, 194, 326, 383, 885, 1366, 1418, 2016, 2042, 2147, 2239, 2334, 2345, 2728, 2761, 2994, 3212, 3321, 3424, 3439]
target = 2042

# Function call
result_iterative = binary_search(target, list)
result_recursive = binary_search_rec(target, list)
 
if result_iterative != -1:
    print("Element is present at index:", str(result_iterative),"(Iterative binary search)")
else:
    print("Element is not present in array")

if result_recursive != -1:
    print("Element is present at index:", str(result_recursive),"(Recursive binary search)")
else:
    print("Element is not present in array")