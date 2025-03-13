# following are the collections
# list, tuple, set, dict, namedtuple, deque, Counter, OrderedDict, defaultdict
#
# list example
from collections import namedtuple, deque, Counter, OrderedDict, defaultdict
from itertools import count

fruits = ["apple", "orange", "banana"]

fruits.append("mango")
print(fruits)

# Tuple is ordered immutable collections
coordinates = (10,20,15)

print(coordinates)

# Set is unordered collection of unique item
colors={"red", "green", "blue"}
colors.add("black")
colors.add("red")

print(colors)

# Dictionary (dict) unordered collection of key value pairs.

person = {"name": "alice", "age": 30, "phone": "1234567890"}
person["age"]=20
print(person)

# collections from collection module
# namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(10,20)
print(p.x,p.y)

# deque
# double ended queue allowed fast appends and pops from both end

d= deque([1,2,3])
d.append(4)
d.appendleft(0)
print(d)
d.pop()
print(d)

# counter is a dictionary subclass which count the number of occurrences of elements in list

items = ["apple", "banana", "apple", "orange", "banana","banana"]
counter = Counter(items)
print(counter["apple"])

# Ordered dict
# dictionary that maintains the order of the keys as they are inserted.

ordered_dict= OrderedDict()
ordered_dict["two"] =2
ordered_dict["one"]=1
ordered_dict["three"]=3
print(ordered_dict)

# default dict
def_dict= defaultdict(int)
def_dict["apple"] +=1
def_dict["banana"] +=2
print(def_dict)

