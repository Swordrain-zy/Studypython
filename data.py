from lib2to3.pytree import convert

from sympy import false, true


#integer convert
a=30
print(bin(a))
print(oct(a))
print(hex(a))

#min max
a=3;b=4;c=5
print(min(a,b,c))
print(max(a,b,c))

#float bool complex
a=5.023
b=false
c=2+3j
d=9
print(type(a),type(b),type(c),type(d))
print(round(a,2),round(a,1))
import math
print(math.floor(5.6))
print(math.ceil(5.6))
print(c.real,c.imag,abs(c),abs(-5))

#string
fruit="banana"
print(fruit,len(fruit),len("apple"))
for i in range(6):
    print(fruit[i])
print(type(fruit))
