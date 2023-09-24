"""
1. Create a list with 6 different integer or float values and multiply all items in the list with each other
Expected result: one integer or float value
"""
### insert code here
list1 = [12, 45, 67, 2, 9,24]
# multiply = 1
# for li in list1:
#     multiply *= li
# print(multiply)

#oder
import functools as ft
multiply = ft.reduce(lambda a, b: a*b, list1)
print(multiply)