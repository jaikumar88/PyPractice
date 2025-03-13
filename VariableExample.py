# Python variables

# Python has Integer(Int): which contains whole number
# Floats(float): Decimal numbers
# String (str): Text string
#Booleabs (bool): True or False
# Lists(list): Ordered collections of items

# Integer E.g
i = 10

print(i)

# Float eg
price = 15.73

print(price)

#String
name="Alice"
print(name)


reverse_name=""
for char in name:
    reverse_name = char + reverse_name
print(reverse_name)

reverse_name=""
#using a Stack (List)
stack=list(name)
while stack:
    reverse_name+=stack.pop()
print(reverse_name)

#Boolean
isActive=True
print(isActive)

#List
fruits=["apple", "banana", "mango"]
print(fruits)

#Tuple
coordinate = (1,8)
print(coordinate)

#Dictionary a key value pair in Python

person={"name": "Bob", "age": 20}
print(person)

#Set
colors={"green", "red", "yellow"}
print(colors)

for c in colors:
    print(c)

#None Type
result=None
print(result)

