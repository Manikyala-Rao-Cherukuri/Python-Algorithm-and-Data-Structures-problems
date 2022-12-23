def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        for i in range(1, len(array)):
            if array[i] <= pivot:
                less.append(array[i])
            else:
                greater.append(array[i])
    return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10,99,2,31,4,1,8,9,0,111]))
