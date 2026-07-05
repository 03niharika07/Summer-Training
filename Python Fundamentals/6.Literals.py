# LITERALS
'''Literals are the data items that have a fixed/constant value
Example : a=2, here a is variable, = is operator and 2 is literal'''

# TYPES OF LITERALS
'''
1. Numeric Literals
2. String Literals
3. Boolean Literals
4. Special Literal None
'''

# 1. NUMERIC LITERALS

a = 0b1010      # binary literal
print(a)
b = 100         # decimal literal
print(b)
c = 0o310       # octal literal
print(c)        
d = 0x12c       # hexadecimal literal   
print(d)

# float literal 
float_1 = 10.6
float_2 = 1.5e2       # 1.5*10^2
float_3 = 1.5e-3      # 1.5*10^-3

print(float_1)
print(float_2)
print(float_3)

# complex literal
x = 3.14j
print(x)
print(x.real,x.imag)


# 2. STRING LITERALS

# single line strings
str = "This is python"
str2 = 'This is Python'
print(str)
print(str2)

# multi line strings
str3 = '''Hello
Python Language
Learning'''
print(str3)

str4 = """Learning Python
Python Fundamentals"""

char = "C"
print(char)
# for emoji , unicode is used
unicode = u"\U0001F600"
print(unicode)
raw_str = r"raw \n string"
print(raw_str)


# 3. BOOLEAN LITERAL

a = True + 4         # returns 5 bcoz true is 1
b = False + 10       # returns 10 bcoz false is 0
print("a:",a)
print("b:",b)


# 4. SPECIAL LITERAL None

a = None
print(a)