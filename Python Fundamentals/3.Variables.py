# VARIABLES (containers for future, tells the location for the storage)

# create/declare a variable
name = "Python"       # no need to specify data type in python
# use a variable
print(name)

a = 5
b = 19
print(a + b)

# DYNAMIC TYPING VS STATIC TYPING
'''Dynamic Typing : In python , we do not specify the data type while declaring a variable.
Dynamic typing means declaring a variable without telling the data type.
It automatically understands 
Python supports dynamic typing
Static Typing : In this, data type is specified at the time of declaration.'''

# DYNAMIC BINDING VS STATIC BINDING
'''Dynamic Binding : The data type is not fixed at the compile time, decided at the runtime.
Python supports dynamic binding.
Static Binding : The data type is fixed at the compile time.
C/C++/Java supports static binding  (Example int a=5)'''

a = 5
print(a)
a = "Neha"
print(a)
print('\n')

# ways to write variables
a,b,c = 10,20,30
print(a,b,c)

a=b=c = 5
print(a,b,c)
