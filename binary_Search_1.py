none = 'Out of range'
def binary_search(my_list, item):
    low = 0
    high = len(my_list)-1
    while low <= high:
        mid = round((low+high)/2)
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return none

my_list = [1,3,5,7,9]
item =int(input("please enter the number between 1 to 9: "))
v = binary_search(my_list, item)
print("Index of your guessed value from the list is: {0}".format(v))
