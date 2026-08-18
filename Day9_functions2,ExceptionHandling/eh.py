'''
Error: When a program is encoutered with error. The program will be terminated
Bug: is a logical errors developed by the programers
Types of errors:
1. systanx error
2. Logical error
3. runtime error


value error
name error
type error
zerodivision

try : 
except: 
else
finally
'''
try:
    a=int(input('Enter the a value'))
    b=int(input('Enter the b value'))
    
except Exception as e:
    print(e)
else:
    if a%b==0:
        print('even')
    else:
        raise ValueError('Please enter values to genarate even number')         
finally:
    print('Th program is completed')