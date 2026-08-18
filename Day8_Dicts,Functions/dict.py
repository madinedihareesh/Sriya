'''
Dict a key and value paired datatype.it is mutable
'''
d={1:'One','two':2,12+9j:'cpm[lex',12.54:'float','isloggedin':True} ##literal style
'''
zip
enumarate
'''
lt=[(1,'one'),(2,'two'),(3,'three'),(4,'four')] ## explicit paired data
d1=dict(lt)
print(d1)

l=[1,2,3,4,5]
l1=['one','two','three','four','five']

com=zip(l,l1)
d2=dict(com)
print(d2)

d3=dict(enumerate(l1,start=100))
print(d3)


d4={}
print(type(d4))
d4['one']=1
print(d4)

print(dir(dict))

'''
Dict methods

'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
'''

# print(dict.fromkeys([1,2,3,4,5]))
print(d['two'])
print(d.get('two'))
print(d.items()) ## paired values
print(d.keys()) ## keys from dict
print(d.values()) ## values from dict
d2.pop(5) ## spacified key to remove the item from dict
print(d2)
d2.popitem()
print(d2)
# d2[4]='four'
# print(d2)

d2.update({4:'four',5:'five',6:'six'})
print(d2)

# d2.setdefault(6,'sixty')
# print(d2[6])

d2.clear()
print(d2)
del(d2)

d2=d.copy()
print(d2)


d4={x:y for x,y in zip(l,l1)}
print(d4)

d5={x:y for x,y in lt}
print(d5)

d6={x:y for x,y in enumerate(l1,start=100)}
print(d6)


