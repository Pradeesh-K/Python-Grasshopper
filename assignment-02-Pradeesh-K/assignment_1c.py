"""
1c. Define a function for computing the cross products of two same-length lists of vectors
"""

from compas.geometry import cross_vectors

v1 = [[0.0, 1.0, 2.0],[3.0, 4.0, 5.0],[6.0, 7.0, 8.0]]
v2 = [[8.0, 7.0, 6.0],[5.0, 4.0, 3.0],[2.0, 1.0, 0.0]]

def xproductarray(array1, array2):
    # Insert code here
    if(len(array1) == len(array1)):
        xproducts = []
        for i in range(len(array1)):
            xproducts.append(cross_vectors(array1[i],array2[i]))
        return xproducts
    else:
        print('Arrays are not equal in length')
        return None
    #return xproducts

print(xproductarray(v1, v2))