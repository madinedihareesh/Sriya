'''
print the digit in a numbers 
print sum of the digits in a number
print the pallendrome of a number
print th chars in a string
print * if there are any vowels in a string insted of vowels
print number of factors for a number
find wether a number is a prime number or not
print prime numbers in between 1 to 100
print even numbers in between 1 to 100
fibbanocci
leap year
1234
'''
'''num=1234
while num>0:
    res=num%10
    print(res)
    num//=10 ##num=num//10'''

'''num=1234
sum=0
while num>0:
    res=num%10
    sum+=res
    num//=10
else:
    print(sum)  ''' 

'''num=int(input('Enter  a number : '))
clone=num
rev=0
while num>0:
    res=num%10
    rev=rev*10+res
    num//=10
else:
    
    if clone==rev:
        print(clone,'is a palendrome')
    else:
        print(clone,'is not a palendrome') '''      

'''s='Hello world' 
i=0
while i<len(s):
    print(s[i])
    i+=1'''

'''vowels='aeiouAEIOU'
s=input('Enter your string: ')
i=0
while i < len(s):
    if s[i] in vowels:
        print('*',end='')
    else:
        print(s[i],end='')
    i+=1  '''      

'''num=9
i=1
count=0
while i<=num:
    if num%i==0:
        print(i)
        count+=1
    i+=1
else:
    print(count)  '''      

'''num=9
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
else:
    if count==2:
        print('prime number')
    else:
        print('composite number')  '''          

'''i=1
while i<101:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    else:
        if count==2:
            print(i,end=',')
    i+=1  '''     

'''i=1
while i<101:
    if i%2==0:
        print(i,'even')
    i+=1  ''' 

'''a=0
b=1
c=0
i=0
while i<11:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1  '''

'''year=int(input('Enter the year'))
if year%100==0:
    if year%400==0:
        print('leap year')
    else:
        print('it is not a leap year')
elif year%4==0:
    print('leap year') 
else:
    print('not a leap year')  '''


'''
*
* *
* * *
* * * *
* * * * *
'''

'''i=1
while i<6:
    j=1
    while j<6:
        if j>=i:
            print('* ',end='')
        j+=1
    print()    
    i+=1    '''


'''
1 
1 2
1 2 3
1 2 3 4 
1 2 3 4 5

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

A
A B
A B C
A B C D
A B C D E

A
B C 
D E F
G H I J
K L M N O
'''