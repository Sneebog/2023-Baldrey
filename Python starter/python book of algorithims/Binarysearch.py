def binary_search(array, low, high, x):
    if len(array) != 0:
        middle = (high + low) // 2
        if array[middle] == x:
            answer = middle
        elif array[middle] > x:
            answer = binary_search(array, low, middle - 1, x)
        else:
            answer = binary_search(array, middle + 1, high, x)
    else:
        answer = -1
    return answer
testarray = [ 2, 3, 4, 10, 15, 45, 85 ]
variablesearched = int(input("What number are you searching for?"))
result = binary_search(testarray, 0, len(testarray)-1, variablesearched)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")