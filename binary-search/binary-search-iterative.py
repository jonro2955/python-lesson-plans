# Returns index of target in given input_list if present, else returns -1
def binary_search(input_list, target):
    low = 0
    high = len(input_list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If target is greater, ignore left half
        if input_list[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        elif input_list[mid] > target:
            high = mid - 1
        # else, it means target is present at mid
        else:
            return mid
    # If we reach here, then the Target was not present
    return -1


# Test
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Target is present at index", str(result))
else:
    print("Target is not present in array")
