arr_list = [5,3,6,2,9]

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#print("The samllest number in the list is: ",findSmallest(arr_list))

def selectionSort(arr):
    new_arr = []
    for i in range(0, len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print("The sorted list is: ",selectionSort(arr_list))
