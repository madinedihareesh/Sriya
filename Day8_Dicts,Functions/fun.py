'''
function:
Function is a block of code that can be invoked/called n no times, by passing diffrent inputs
it is going ganarate output accordingly

simple function
function with return statements
function with multiple return statements
function with parametrs/arrguments
function with positional only arrguments
function wiht keyword only arrguments
mixed postional and keyword arrguments
'''

'''
def nameoffunction():
    block of code
'''
# simple function
'''# declaration of function
def greeting(name):
    print('Hello world '+name)

# invoking a function
greeting('james')
greeting('jason')
greeting('peter')
greeting('wills')
greeting('sam')'''

# with return statements
'''def greet():
    return 'Hello world'

print(greet())

def add(a,b):
    return a+b

print(add(10,20)) 


def math(a,b):
    sum=a+b
    pro=a*b
    diff=a-b
    div=a//b
    mod=a%b
    return sum,pro,diff,div,mod'''


'''def add(a,b,c,d): ## formal arrguments
    print(a,b,c,d)
    return a+b+c+d

print(add(10,20,30,40))  ## actual arrguments

print(add(10,20,30,40)) ## postional arrguments

print(add(d=40,a=30,c=20,b=10)) ## keyword arrguments

print(add(30,40,d=10,c=20)) ## rule: first postional arrguments then keyword'''


# positional only arrguments

'''def add(a,b,c,/): ## '/' we can make positional only arrguments
    return a+b+c

print(add(c=30,a=20,b=10))'''

# key word only arrguments
'''def add(*,a,b,c): ## '*' infront of arrguemnts we can declare keyword only arrguemnts
    return a+b+c

print(add(c=10,b=20,a=30))'''

# mixed postional and keyword arrguments
'''def add(a,b,/,*,c,d):
    return a+b+c+d

print(add(10,20,d=40,c=30))'''
