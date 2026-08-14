'''
def of list:
is mutable  ordered collection of hetroginous elemnts, it allows duplicates
'''
'''l=[1,'james',True,12.54,12+9j,1,12.54]
print(l[0])
print(id(l))
print(id(l[1]))
print(id(l[0]))
print(id(l[2]))
l.append(11)
print(l)
print(id(l))'''

'''
# list traversing
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i)
'''

'''
# list sum and product
l=[1,2,3,4,5]
l1=[6,7,8,9,10]
print(l+l1)
print(l*3)'''

'''
Slicing:
u,r,i
'''
'''l=[1,2,3,4,5,6,7,8,9,10]
# reading
l1=l[::]
print(l1)
# update/replace
l[0]=11
print(l)
# inserted/replace a group of values
l[0:2]=[101,102]
print(l)'''

# ways to create a list
# l=[1,2,3,4,5,6,7,8]
# l1=list((1,2,3,4,5,6))
# print(type(l1),l1)
# l2=list('python')
# print(type(l2),l2)
# l3=[]
# print(type(l3))

'''
methods of list
Adding
finding
formating
sorting and revarse
deleting
'''
# Adding
# l=[1,2,3,4,5]
# l.append(6) ## single value can be added to a list
# print(l)
# l.extend([7,8,9,10]) ## group of elements to list
# print(l)
# l.insert(0,6)
# print(l)

# l=[1,2,3,4,5,6,2,2]
# print(l.index(3))
# print(l.count(2))

# l=[100,90,70,60,80,50,20,40,10,30]
# l.sort(reverse=True)
# print(l)

# l=[1,2,3,4,5,6]
# l.reverse()
# print(l)

'''# pop
l=[1,2,3,4,5,6,7,8]
l.pop()
print(l)
l.remove(2)
print(l)

l1=l ## Deep copy
print(id(l1),id(l))
l2=l.copy() ## Hellow Copy
print(id(l2),id(l))

l.clear()
print(l1)
print(l2)'''

'''
l=[1,2,3,4,5]
print(sum(l))
print(min(l))
print(max(l))
'''

'''l=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
for i in range(0,3):
    for j in range(0,3):
        print(l[i][j]+l2[i][j],end=' ')
    print() '''     


'''l=[]
for i in range(1,11):
    i=i**2
    l.append(i)

print(l)'''

# list comp l=[exp for item in seq]
l=[x**2 for x in range(1,11)]
print(l)