__author__ = 'jc437351'

"""

"""
valid = False
while  not valid:
    name = input("Enter your name:")
    if name != "" and not name.isspace():
        valid = True
print(valid)

l = len(name)
for i in range(0, l, 2):
    print(name[i])
