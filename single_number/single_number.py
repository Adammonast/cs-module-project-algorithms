'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # keep an array to hold numbers we see in the numbers array
    no_duplicates = []
    # iterate through numbers
    for x in arr:
        # check to see if the number is already in the created array
        if x not in no_duplicates:
            no_duplicates.append(x)
        # if it is, remove it from array
        else:
            no_duplicates.remove(x)
    # when iteration is done, the only number in the array is the odd number out
    # return odd number
    return no_duplicates[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
