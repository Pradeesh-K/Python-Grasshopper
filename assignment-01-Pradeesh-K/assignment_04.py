"""
4. Write a function that returns the largest number from an input list
"""

def find_largest_number(numbers):
    ## return - commented it out as it prevented the function from running
    ### insert code here
    max_no = 0
    for number in numbers:
        if(number > max_no):
            max_no = number
    return max_no
    # #oder
    # return max(numbers)


input_list = [23, 5, 9, 28]
b = find_largest_number(input_list)
print(b)
