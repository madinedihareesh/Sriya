'''
tuple is immutable ordered collection of elemnts 
it allows duplicates
'''
# t=(1,12.34,True,'james',1) ## litral way
# print(type(t))
# print(t[0])

# types of creating tuple
'''t1=tuple('python') ## type converstion
t2=tuple([1,2,3,4,5])
print(t1)
print(t2)
t=()
print(type(t))
t3=(3,) ## single elemnet tuple
print(type(t3))

t4=1,2,3,4,5 ## packing
print(t4)
print(type(t4))

# unpacking
a,b,*c=t4
print(a)
print(b)
print(c)'''

'''
t=(1,2,3,4,5,6)
t1=t[::-1]
print(t1)'''

'''t=(1,2,3,4,5)
for i in t:
    print(i)'''

'''t=(1,2,3,4)
t1=(5,6,7,8)
print(t+t1)
print(t*3)'''

# Methods of tuple
'''print(dir(tuple))

t=(1,2,3,4,5,6,1,2,1)
print(t.count(1))
print(t.index(5))'''

# Aggrigate functions on tuple
'''
t=(1,2,3,4,5,6,7,8,9,10)
print(sum(t))
print(max(t))
print(min(t))
'''

# tuple comprehensions directly possible 
t=(*(x for x in range(1,11)),) ## grnatator + unpacking method
print(t)

t1=tuple([x for x in range(1,11)])

print(t1)
