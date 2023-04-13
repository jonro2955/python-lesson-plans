def bubble_sort(arr):
    length = len(arr)
    # keep track of whether the array is already sorted
    swapped = False
    # traverse through all but the last item
    # if there are 10 items, index i in range(length - 1) only goes up to 8
    for i in range(length - 1):
        # for each i, traverse the array from 0 up to length-i-1
        for j in range(0, length - i - 1):
            # swap if element j'th element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print("swapping", arr[j], "with", arr[j + 1])
        print("pass", i, ":", arr)
        if not swapped:
            # if no swap took place, we can just exit the main loop
            return


# Test
test_arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(test_arr)
print("Sorted array:", test_arr)
# Sorted array should be: [11, 12, 22, 25, 34, 64, 90]
# Time Complexity: O(n2).
# Auxiliary Space: O(1).
