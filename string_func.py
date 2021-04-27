#  string functions

a = [1, 2, 3, 4]
b = 'hello world'
c = 'HELLOWORLD'
x = '123'
y = '123abcd'
z = '#$%122nhhfh'
m = 'Hello World'

A = a
print(A)
d = a.copy()
print(type(d), "\n")
print(id(d), id(a), id(A))
print(d)
print(1 in a)
print(10 in a)
print(10 not in a)
print(1 not in a)
print(b.capitalize())
print(b.startswith('h'), b.startswith('n'))
print(b.endswith('h'), b.endswith('d'))
print(z.isalpha(), y.isalpha(), b.isalpha(), c.isalpha())
print(type(b), type(x))
print(x.isdigit(), y.isdigit())
print(z.isalnum(), y.isalnum())
print(c.islower(), b.islower())
print(c.isupper(), b.isupper())
print(b.istitle(), c.istitle(), m.istitle())
print(c.lower())
print(b.upper())
print(c.title(), b.title())
print(c.find('W'), c.find('w'), c.find('m'))
print(b)
print(b.replace('world', 'universe'))
print(b.split('h'), b.split(' '), b.split('w'), b.split('d'))  # return list
print(' '.join(c), '_'.join(c))
print(len(c))
print(b[::2])
print(b[::-1])
print(b[::1])
