'''
set is a mutable unordered collection of hetroginous elemts 
it can not accpect duplicates

'''
# s={1,'james',True,12.34,12+9j} ## Litaral way of set 
# print(s)

'''for i in s:
    print(i)'''
# ways to create sets
'''
s1=set('python')
print(s1)
s2=(set([1,2,3,4,5,6]))
print(s2)
s3=set()
print(type(s3))
'''
# print(dir(set))

''' 
'add',
 'clear',
   'copy',
     'difference',
       'difference_update',
         'discard', 'intersection',
           'intersection_update',
             'isdisjoint',
               'issubset', 
               'issuperset', 
               'pop',
                 'remove',
                   'symmetric_difference',
                     'symmetric_difference_update',
                       'union', 
                       'update'
'''
# s={1,2,3,4,5,6}
# s.add(7)
# print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

# union
'''print(s1|s2)
print(s1.union(s2))
s1|=s2
print(s1)'''

# intersection
'''print(s1&s2)
print(s1.intersection(s2))
# s1&=s2
# print(s1)
s1.intersection_update(s2)
print(s1)'''

# diffarence
'''print(s1-s2)
print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)
s1-=s2;print(s1)'''

# semathic diffarence
'''print(s1^s2)
print(s1.symmetric_difference(s2))
# s1^=s2
# print(s1)
s1.symmetric_difference_update(s2)
print(s1)'''

# s1.pop()
# print(s1)

# s1.remove(4)
# print(s1)

# s={1,2,3,4,5,6,7,8,9,10}

# print(sum(s))
# print(min(s))
# print(max(s))


s={x for x in range(1,11)}
print(s)