# if example

x=10
if x > 5:
    print("x is greater then 5")

# if else
x = 3
if x > 5:
    print("x is greater then 5")
else:
    print("x is less then 5")

# nested

name="alice"
if name == "alice":
    print("name is alice")
elif name == "ram":
    print("name is ram")

# For loop

fruits = ["apple", "orange", "banana"]
for fruit in fruits:
    print(f"Fruits:{fruit}")

for i in range(2):
    print(i)

# while loop
z=0
while z < 5:
    print(z)
    z +=1

# break statement
for i in range(1000):
    if i == 2:
        break
    print(i)

# continue
for i in range(7):
    if i==5:
        continue
    print(i)

# else with loop
for i in range(5):
    print(i)
else:
    print("Loop finished")

