'''
Variable length postion arrguemnts
'''
'''def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum    


op=add(1,2,3,4,5,6) 
print(op) '''  

'''
Variable length keyword arrguments
'''
'''customers=[]
def personinfo(**kwargs):
    for i in kwargs:
        print(f'{i}:{kwargs[i]}')
    customers.append(kwargs)    

personinfo(name='james',age=31,loc='Hyd',email='james@gmail.com')
print(customers)'''

'''
Nested function
'''
'''def outter():
    print('+'*10)
    def inner():
        print('This is a inner function')
    return  inner

op=outter()
op() '''   

'''
Clouser

ans: when the inner function have the ability to read the variables and
parameter from outter function then inner function is known as clouser

'''
'''def outter():
    name='james'
    def inner():
        print(name)
    inner()

outter()'''

'''def outter(name):
    def inner():
        print(name)
    inner()

outter('james') '''     


'''
Higher Order Function

if a function has a ability to read another function as parameter 
'''

'''def Sample(f):
    print('+'*10)
    f()
    print('*'*10)

def Greeting():
    print('Hello world')

Sample(Greeting)'''

'''
if a function is calable from another function is know as call back function
'''




