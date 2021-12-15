# Run this python script it will split and get the last dict value

def getObjectKey(o, k):
    sp = k.split('/')
    return o[sp[0]][sp[1]][sp[2]]

objc = {'a':{'b':{'c':'d'}}}
key_val = 'a/b/c'
print(getObjectKey(objc, key_val))

objc = {'x':{'y':{'z':'a'}}}
key_val = 'x/y/z'
print(getObjectKey(objc, key_val))
