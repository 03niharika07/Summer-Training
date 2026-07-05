# Q1 :- Print the given strings as per stated format.
# Given strings:
# "Data" "Science" "Mentorship" "Program" 
# "By" "CampusX" 
# Output:
# Data-Science-Mentorship-Program-started-By-CampusX

print("Data","Science","Mentorship","Program","By","CampusX",sep='-')
print('\n')

# Q2:- Write a program that will convert celsius value to fahrenheit.

celsius = float(input("Enter celsius value: "))
print("Celsius:",celsius)

fahrenheit = (celsius*(9/5))+32
print("Fahrenheit:",fahrenheit)
print('\n')

# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

a = int(input("Enter first no: "))
b = int(input("Enter second no: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After Swapping:")
print("a =", a)
print("b =", b)

