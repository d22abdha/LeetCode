def binary_search(lst, n, key):
    first = 0
    last = n - 1

    while first <= last:
        middle = (first + last) // 2
        value = lst[middle]

        if key == value:
            return middle
        else:
            if key < value:
                last = middle - 1  # search in the left half
            else:
                first = middle + 1  # search in the right half

    return -1  
 

# Now use the function
arr = [1, 3, 5, 7, 9, 11]
key = 11
index = binary_search(arr, len(arr), key)

print("Found at index:" if index != -1 else "Not found", index)
