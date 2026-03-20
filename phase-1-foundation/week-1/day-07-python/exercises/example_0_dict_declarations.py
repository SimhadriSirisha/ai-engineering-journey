a = dict(one = 1, two = 2, three = 3) #keyword argument syntax - (keys must be valid identifiers → become strings)
b = {'one' : 1, 'two' : 2, 'three' : 3} #dict literal syntax
c = dict([('two', 2), ('one', 1), ('three', 3)]) #list of tuples (any hashable type as key)
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
e = dict({'three': 3, 'two': 2, 'one': 1})
print(a == b == c == d == e)
