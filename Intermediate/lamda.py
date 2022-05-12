# this is lambda creating of function
add10 = lambda x: x + 10
print(add10(5))

# this is classical way of creating function
def add10_func(x):
    return x + 10

# parsing of two variables in lamdba function
mult = lambda x,y: x * y
print(mult(2,4))



# creating of lists with a tuple embedded inside
points2D = [(1,2),(15,1),(5,-1),(10,4)]
# this will sort the list by "x" argument
# to give specific rule, add some hyperparams
points2D_sorted = sorted(points2D)
points2D_sorted_y = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)
print(points2D_sorted_y)

# map function (func, seq)
from torch import conv_tbc


a = [1,2,3,4,5]
mapping= map(lambda x: x * 2, a)
print(list(mapping))

# convential way of mapping 
conv_mapping = [x*2 for x in a]
print(conv_mapping)

# it filter the elements in list based on
# function calculation
filtering = filter(lambda x: x%2==0,a)
print(list(filtering))

from functools import reduce

# this function reduces the list into single value
# based on the calculation of function.
product_a = reduce(lambda x,y: x + y, a)
print(product_a)