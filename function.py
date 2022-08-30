#definition
def funcname (para1,para2):
    '''documentation string'''
    #<body of the function>

#instance:
def add(x1,x2):
    '''return the sum of x1&x2'''
    return x1+x2

#call
a=10
b=12
result=add(a,b)
print(result)

#return value
#instance:fibonacci array
#define fib()
def fib(n):
    '''Print a Fibonacci series up to n'''
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
        print()
#call fib()
fib(20)
f=fib #rename
f(20)
#fib() does not return any value because of it does not have any 'return'
#define fib1()
def fib1(n):
    '''Print a Fibonacci series up to n'''
    a,b=0,1
    result=[]
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result
#result array will be return by a list
#lambda function
add_one=lambda x:x+1
add_one(1)#output:2

add_two=lambda x,y:x+y
add_two(3,4)#output:7
#end


