# USER INPUT
''' Input function is used to take input from user'''

# Static Vs Dynamic
'''In static, ony info is taken.
In dynamic, user input is taken like youtube'''

# PROGRAM 1: SUM OF 2 NO.S

# take input from user and store them in variable
# add two variables
# print result
a = int(input("Enter first no. : "))
b = int(input("Enter second no. : "))
result = a+b

print("Sum of",a,"and",b,"is",result)

# By default input function is string
# Bcoz other data types can be stored in string
num = input("Enter Number : ")
print(type(num))    # string


# TYPE CONVERSION
# (converting one data type to the other)
# Implicit vs Explicit
''' Implicit Type Conversion : automatically done by the compilers
Explicit Type Conversion : done by the programmers'''

# Example - Implicit
print(5+5.6)

# Example - Explicit
# print(4 + '4')         # show error

# str -> int
print(int('4'))
print(type(int('4')))

# print(int(5+4j))        # show error, cannot be converted to int

# int -> str
print(str(5))

# int -> float
print(float(4))


x =input("Enter first no. : ")
y =input("Enter second no. : ")
result =  int(x)+(int)(y)  # does not change original value, creates new in which changes are made

print("Sum of",x,"and",y,"is",result)
print(type(result))
print(type(x))