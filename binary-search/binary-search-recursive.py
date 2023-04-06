# Returns index of target in arr if present, else -1
def binary_search(input_list, low, high, target):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If Target is at the middle, return the mid-index
        if input_list[mid] == target:
            return mid
        # If Target is smaller than mid, then recursively call parent function with left subarray
        elif input_list[mid] > target:
            return binary_search(input_list, low, mid - 1, target)
        # Else the Target can only be present in right subarray
        else:
            return binary_search(input_list, mid + 1, high, target)
    else:
        # Target is not present in the array
        return -1


# Test
my_list = [2, 3, 4, 10, 40]
x = 10
result = binary_search(my_list, 0, len(my_list) - 1, x)
if result != -1:
    print("Target is present at index", str(result))
else:
    print("Target is not present in array")
