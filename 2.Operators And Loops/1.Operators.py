# OPERATORS

# TYPES OF OPERATORS
'''
1. Arithmetic
2. Relational
3. Assignment
4. Logical
5. Bitwise
6. Membership
7. Identity
'''

# 1. ARITHMETIC OPERATORS (+,-,*,/,//,%,**)
print(5+6)
print(2-3)
print(7*8)
print(13/6)    # returns quotient
print(13//6)   # floor division (int division), returns quotient(int part)
print(2**3)    # exponential operator(power of operator)
print(5%2)     # returns remainder

# 2. RELATIONAL OPERATORS (>,<,>=,<=,==,!=)
print(5>7)
print(4<6)
print(4>=4)
print(4<=9)
print(3==3)
print(6!=0)

# 3. LOGICAL OPERATORS (and,or,not)
print(1 and 0)
print(1 or 0)
print(not 0)

# 4. BITWISE OPERATORS (operated on binary values)
print(2 & 3)    # bitwise and
print(2 | 3)    # bitwise or
print(2 ^ 3)    # bitwise xor (different values p 1)
print(~3)       # bitwise not
print(4 >> 2)   # bitwise right shift (divide by 2)
print(5 << 2)   # bitwise left shift (multiply by 2

# 5. ASSIGNMENT OPERATORS
a = 2
a +=2
print(a)
a -=2
print(a)
a *=2
a /=2
a %=2
a **=2
print(a)

# 6. MEMBERSHIP OPERATORS (in, not in)
print('D' in 'Delhi')
print('d' in 'Delhi')     # false, case sensitive
print('d' not in 'Delhi') 
print(1 in [1,23,4,5])

# 7. IDENTITY OPERATORS (is, is not)
'''Identity operators are used to check if both the operands refer to the 
same memory location and returns true if both the operands refer to the same memory location
else return false'''

a = 10
b = 10
print(a is b)        # true

# lists are mutable ( 2 diff lists are formed)
c = [10,20]
d = [10,20]
print(c is d)        # false (diff memeory location)


# Find the sum of a 3 digit number entered by the user
num = int(input("Enter 3 digit number : "))

a = num%10         # 345%10 -> 5
num = num//10      # 34

b = num%10         # 34%10 -> 4
num = num//10      # 3

c = num%10         # 3%10 -> 3

print("Sum of digits:",a+b+c)