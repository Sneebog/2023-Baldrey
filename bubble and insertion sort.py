def bubblesort(array):
    n = len(array)
    count = 0
    for i in range(0, n):
        count += 1
        for j in range(0, n - i -1):
            count += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                count += 1
    print(count)
    return array
def insertionsort(array):
    n = len(array)
    count = 0
    for j in range(1, n):
        count += 1
        nextNum = array[j]
        i = j - 1
        while i >= 0 and array[i] > nextNum:
            array[i + 1] = array[i]
            i -= 1
            count +=1
        array[i + 1] = nextNum
    print(count)
    return array
testarray = [6,8,2,4,9]
testarray2 = [6,8,2,4,9]
bubblesort(testarray)
insertionsort(testarray2)
print(testarray)
  