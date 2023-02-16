# 1
username = input("Enter username:")
print("Username is: " + username)

"""username = raw_input("Enter username:")
print("Username is: " + username)"""





# 2
print("Hello, World!")





#3
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

x = 5
y = "Hello, World!"

#This is a comment.
print("Hello, World!")





#4
#example 1
x = 5
y = "John"
print(x)
print(y)
#example 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#example 3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#example 4
x = 5
y = "John"
print(type(x))
print(type(y))
#example 5
x = "John"
# is the same as
x = 'John'
#example 6
a = 4
A = "Sally"
#A will not overwrite a





#5
x = 5
print(type(x))





#6
# example 1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# example 2
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# example 3
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#example 4
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
# example 5
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#example 6
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#example 7
import random

print(random.randrange(1, 10))





#7
#example 1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#example 2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#example 3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'






#8
#example 1
print("Hello")
print('Hello')
#example 2
a = "Hello"
print(a)
#example 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#example 4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#example 5
a = "Hello, World!"
print(a[1])
#example 6
for x in "banana":
  print(x)
#example 7
a = "Hello, World!"
print(len(a))
#example 8
txt = "The best things in life are free!"
print("free" in txt)
#example 9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#example 10
txt = "The best things in life are free!"
print("expensive" not in txt)
#example 11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")





#9

#example 1
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#example 2
txt = "The price is {:.2f} dollars"
#example 3
print(txt.format(price, itemno, count))
#example 4
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#example 4
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#example 5
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
#example 6
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



#10

#example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#example 3
print(bool("Hello"))
print(bool(15))
#example 4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#example 5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#example 6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#example 7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#example 8
def myFunction() :
  return True

print(myFunction())
#example 9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#example 10
x = 200
print(isinstance(x, int))



#11
print(10 + 5)


#12

#example 1
a = 33
b = 200
if b > a:
  print("b is greater than a")
#example 2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#example 3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#example 4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#example 5
if a > b: print("a is greater than b")
#example 6
a = 2
b = 330
print("A") if a > b else print("B")
#example 7
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#example 8
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#example 9
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#example 10
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#example 11
a = 33
b = 200

if b > a:
  pass