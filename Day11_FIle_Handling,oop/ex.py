'''
r+
w+
a+

rb
wb

with
'''

# with open('sample.txt','w') as f:
#     f.write('''Hi there!
# Hello world
# How are you doing
# i am doing grate
# hope you are doing grate''')


# with open('sample.txt','r+') as f:
#     data=f.read()
#     print(data)
#     print(f.tell())
#     f.seek(2)
#     print(f.tell())
#     data=f.read()
#     print(data)
#     f.seek(0)
#     f.write('''\ni am currently learning python''')


# with open('sample.txt','w+') as f:
#     f.write('Hi there!\nHello world\nHow are you doing')
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     data=f.read()
#     print(data)


# with open('sample.txt','a+') as f:
#     print(f.tell())
#     f.write('\ni am doing grate\nhope you are doing fine')
picinfo=None
with open('python.webp','rb') as f:
    data=f.read()
    picinfo=data

with open('pythonclone.webp','wb') as f:
    f.write(picinfo)