"""
2. Write a program to sort a given list, sort based on the last element in each tuple in increasing order.
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

list_1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

### insert code here
# changing the list
# list_1.sort(key=lambda element: element[1])
# print(list_1)
# not changing the list
sorted_list = sorted(list_1, key=lambda element: element[1])
print(sorted_list)
##