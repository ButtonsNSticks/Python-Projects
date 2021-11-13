# You are going to be given an array of integers. Your job is to take that
# array and find an index N where the sum of the integers to the left of N
# is equal to the sum of the integers to the right of N. If there is no index
# that would make this happen, return -1.

def find_even_index(arr):  # define the function
    for i in range(len(arr)):
        # For loop uses the RANGE function to go from 0 to the length of the array.
        if sum(arr[:i]) == sum(arr[i + 1:]):
            # sum() is an inbuilt function in python that adds
            # all the elements in list,set and tuples and returns
            # the value
            # the [:i] will get all of the elements of the array from the start  UP TO BUT NOT INC position i
            # the [i+1] will get all of the elements of the array from the number FROM BUT NOT INC poistion i+1

            return i
    return -1


find_even_index([1, 2, 3, 4, 3, 2, 1])


