'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    """
    From GeeksforGeeks: Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method

    """

    # iterate through the array using enumeration
    for index, i in enumerate(arr):
        # if the arr index is not 0, call .pop() on the element, then call .insert() to insert it in its proper place
        if arr[index] is not 0:
            # removes/returns last value from the list or the given index value
            arr.pop(index)
            # inserts a given element at a given index in a list
            arr.insert(0, i)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
