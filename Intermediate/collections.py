from collections import Counter,namedtuple,defaultdict, deque
# the above module is imported to count the values

# assigning of string variable
a = "aaacccbbbbbddddee"

# using of counter function to count number of chars.
# it will displya in descending order based on counts.
my_counter = Counter(a)

#display the number of character counts
print(my_counter)

#display the items in a form of tuple
print(my_counter.items())

# display only the keys of dictionary
print(my_counter.keys())

#display only the values of dictionary
print(my_counter.values())

#it will diplay most common items, 
# if its 2 it will display second most coomon items
print(my_counter.most_common(1))

# convert the string into elements to list
print(list(my_counter.elements()))


# using of named tuple
# creating of tuples object
Point = namedtuple('Point',['x','y'])
# parsing of values into tuple form
pt = Point(1,-4)
print(pt)
# for accesing the specific value
print(pt.x,pt.y)


# using of default dict module

# assigning of dicitionary varaibles
# setting of keys and values
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)

# using of deque
#  A double-ended queue, or deque, has the feature of 
# adding and removing elements from either end. 
a = deque()
a.append(1)
a.append(2)
a.append(3)
# adding of elements on left
a.appendleft(0)

# extending element
a.extendleft([-1,-2,-3])

# rotate the elements
a.rotate(-1)
print(a)