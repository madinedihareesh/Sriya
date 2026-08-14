'''
Prefix and sufix
'''
'''s='Python is easy to learn'
print(s.startswith('Py'))
print(s.endswith('arn'))
print(s.removeprefix('Python'))
print(s.removesuffix('learn'))

email='example@gmail@.com'
print(email.rpartition('@'))'''

'''
Heading
'''
'''s='hello world'
s1='HELLO WORLD'
s2='Hello World'

print(s.upper())
print(s1.lower())
print(s.title())
print(s.capitalize())
print(s2.swapcase())
print(s1.casefold())'''

'''
Enq
'''

'''
Escape sequenes

'''
# s='hi there!\nHello wrold\nhow are doing\ni am doing grate\nhow about you'
# print(s)

# \n next line
# \t tab space
# \r carrige return

'''
formating string

3 types:
c-style 
format
formated string
'''
product='SSD'
size=250
price=109.54

print('I am planning to purchase ',product,' size of ',size,' GB cost around ',price)

# c-style formatting
'''
%s string
%d %i int
%f %F %g
'''
print('I am planning to purchase %s size of %i GB costs around $%g'%(product,size,price))

print('i am planning to purchase {} size of {} GB costs around ${}'.format(product,size,price))
print('i am planning to purchase {2} size of {0} GB costs around ${1}'.format(size,price,product))
print(f'i am planning to purchase a {product} size of {size} GB costs around ${price}')

'''
JAMES
james
'''