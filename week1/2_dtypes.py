# integer
x = 1
print(type(x), x)

# float
x = 1.0
print(type(x), x)

# string
x = '1'
print(type(x), x)

# boolean
x = True
print(type(x), x)

# casting
x = int('1')
print(type(x), x)

x = float('1')
print(type(x), x)

x = str(1)
print(type(x), x)

x = bool(1)
print(type(x), x)

# list
x = [1,2,3,4,5]
x.append(6)
x.extend([7,8,9])
x.insert(0,'0')
print(x)

# tuple
x = (1,2,3,4,5)
print(x)

# set
x = {1,2,3,4,5}
x.add(6)
x.update([7,8,9])
x.update([7,8])
print(x)

# dictionary
x = {'a':1, 'b':2, 'c':3}
x['d'] = 4
x.update({'e':5})
x['a'] = 'a'
print(x)


# et cetra
print(list(range(1,9,2)))
print(type(None))
