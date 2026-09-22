print("hello world")
age=22
name="KAJAL "
print(name)
print(age)
print(type(age))

#arithmetic
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3

#relational/comparison
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True

#assignment
a = 10

a += 5    # a = 15
a -= 3    # a = 12
a *= 2    # a = 24
a /= 4    # a = 6.0


#logical

age = 22

print(age > 18 and age < 30)   # True
print(age < 18 or age == 22)   # True
print(not age > 18)            # False

#type casting
x = "10"

print(int(x))       # String → Integer
print(float(x))     # String → Float
print(str(10))      # Integer → String
print(bool(1))      # Integer → Boolean

#input type
marks=input("enter marks :" )
print(marks)