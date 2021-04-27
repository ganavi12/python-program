from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
# a = "aaabbdddccll"
# a = [1, 2, 3, 33, 44, 1, 2, 33]
# print(Counter(a))
# print(Counter(a).keys())
# print(Counter(a).values())
# print(Counter(a).items())
# print(Counter(a).most_common())
# print(Counter(a).most_common(1))

# p = namedtuple('test', 'x,y,z')
# 'test' is a class and x,y,z are parameters
# print(p(1, 3, 4))
# b = p(1, 3, 4)
# print(b.x, b.y, b.z)

# d = defaultdict(int)
# d = {'a': 1, 'b': 2}
# print(d.popitem())


d = deque()
d.append(1)
d.append(10)
print(d)

d.appendleft(2)
print(d)

d.popleft()
print(d)

d.extend({33, 44, 55})
print(d)

d.extendleft([66, 7, 8])
print(d)

d.clear()
print(d)
