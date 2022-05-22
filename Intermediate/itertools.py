# itertools : used insted of for loop for optimization

from itertools import product,permutations,combinations,accumulate,groupby

# create two list
a = [1,2,3]
b = [3,4]

# output:[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
prod = product(a,b)
print("product = ",list(prod))

# premutations return all possbile ordering of the inputs
# like mathematics
perm = permutations(a)
print("permutation = ",list(perm))

# this chooses two numbers possible combinations among the inputs
permwithlength = permutations(a,2)
print("premutation based on length = ",list(permwithlength))

# combination will create all possible values,where order does not matter
# [1,2,4] = [2,4,1] = [1,4,2] in the world of combinations
comb = combinations(a,2)
print("combination = ",list(comb))


# this function adds all the values of the previous indices
# [1,2,3] = [0+1,1+2,1+2+3] = [1,3,6]
accum = accumulate(a)
print("accumulation = ",list(accum))

# to perform multiply in accumulate
import operator
acc_mult = accumulate(a,func=operator.mul)
print("Product accumulation = " ,list(acc_mult))

# it groups the elements in one set, that fulls the functions 
# criterias.
d = [1,2,3,4,5]
person = [{'name':'Tim', 'age':25},{'name':'Hey', 'age':25},{'name':'Slo', 'age':28},{'name':'Nin', 'age':28}]

# for list and dictionary
group_obj = groupby(d,key=lambda x:x<3)
group_objs = groupby(person,key=lambda x:x['age']<26)

# outputting of two lists values
for key, value in group_obj:
    print("Group by = ",key,list(value))

for key, value in group_objs:
    print("Group by = ",key,list(value))


# infinite iterator
from itertools import cycle,repeat
# it repeats the digit one for 4 times
for i in repeat(1,4):
    print(i)

# it repeats the cycle on and on
for i in cycle(a):
    print(i)