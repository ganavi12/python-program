a = {'a':'apple','b':'bat'}
print(a.get('a'))
print(a)
print(a.keys())
print(a.values())
# print(a.popitem())
a['c'] = "cat"
# print(a.pop('a'))
c = a.copy()
print(c)
dict = {'a':'aaa','b':{1:'111',2:'2222'},'c':'cat'}
print(dict['b'][1])
b = {'a':'apple','d':'dog','u':[11,22,33,'heelo'],'f':'fox','t':(1,2,3,4),'s':{4,5,6,11,11,22,44,5,55}}
print(b['u'])
print(b['u'][-1])
print(b['u'][2])
print(b['t'])
print(b['t'][-2])
print(b['s'].pop())
print(b['s'])
# set 

a = {1,2,3,4,5}
b={3,4,5,7.9}
c={11,22,33}
print(a.difference(b))
print(b.difference(a))
a.add(1)
print(a)
print(c)
c.clear()
print(c)
del(c)
# print(c)

set1 = {1,1,2,2,2,4,5,6}
set1.remove(1)
set1.discard(10)
set1.pop()
print('------',set1)
