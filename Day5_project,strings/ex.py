'''
'''
# string slicing
'''s='Hi there! Hello world'
print(s[0 :4]) ##string[staring:Ending char+1: step]
print(s[0:6:2])
srev=s[::-1]
print(srev)'''

# methods of a string
'''
find and indexing:

'''
s='hello world'
# find
'''print(s.find('o',s.find('o')+1))
print(s.rfind('o'))
print(s.find('b'))'''

# index
'''print(s.index('o'))
print(s.rindex('o'))
print(s.index('b'))'''


'''
formatting
'''
'''# ljust
print(s.ljust(15,'$'))
#rjust
print(s.rjust(15,'$'))
# center
print(s.center(15,'$'))
# zfill zerofill
print(s.zfill(15))
s1='    Hello world    '
# lstrip
print(len(s1))
print(s1.lstrip())
print(len(s1.lstrip()))
# rstrip
print(len(s1))
print(s1.rstrip())
print(len(s1.rstrip()))
# strip
print(len(s1))
print(s1.strip())
print(len(s1.strip()))'''

'''
Joins and splits
'''
'''s1='abcd'
s2='/'
s3='a-b-c-d'
# join
print(s2.join(s1))
# replace
print(s3.replace('-',','))'''
'''s1='Hello world hi there'
# split
print(s1.split(' ',1))'''

# para='''Hi there how are you
# i am doing grate
# how about you
# are you doing fine
# '''
# print(para.splitlines())

