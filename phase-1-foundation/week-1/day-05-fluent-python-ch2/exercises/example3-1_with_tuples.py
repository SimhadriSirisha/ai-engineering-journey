lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

# Role 2 (tuple as record): position gives the meaning.
# Unpacking: each tuple is (country, id); % uses positions 0 and 1.
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# Unpack by position: first = country, second = id (ignored with _).
for country, _ in traveler_ids:
    print(country)

# tuple unpacking
latitude, longitude = lax_coordinates
print('latitude %s, longitude %s' % (latitude, longitude))

# swapping
t = (6, 1)
a, b = t
print(a)
print(b)

b,a = a,b
print(a)
print(b)

# unpacking with * prefix
print(divmod(20, 8))
t = (10, 5)
print(divmod(*t))
quotient, reminder = divmod(*t)
print(quotient)
print(reminder)

# dummy variable '_' placeholder to ignore the value
a, _ = ('tuple', 'unpacking')
print(a)

# *args : to hold excess arguments, can be places in any order, it no need to be at last 
a, b, *args = range(5)
print(a)
print(b)
print(args)

a, b, *args = range(3)
print(a)
print(b)
print(args)

a, b, *args = range(2)
print(a)
print(b)
print(args)

a, *args, b = range(5)
print(a)
print(b)
print(args)

# Tuple supports nested unpacking, and it works better if unpacking expression follow the same structure
(a, b, (c, d)) = (2, 3, (4, 5))
print(a)
print(b)
print(c)
print(d)