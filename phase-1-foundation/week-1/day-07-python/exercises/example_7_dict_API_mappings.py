d = {'one': 1, 'two': 2, 'three': 3}

#Reading 
print(d['one'])
print(d.get('one'))
print(d.get('four')) # get by key, None if missing (safe)
print(d.get('four', "there is no key with value `four`")) # get by key, "there is no key with value 'four" if missing (safe)
print('one' in d) # True — key existence check

# Viewing
print(d.keys())
print(d.values())
print(d.items())

# Writing (MutableMapping API)
d['four'] = 4 # insert or update
print(d)
d.update({'five': 5}) # merge another mapping in
print(d)
print(d.pop('two')) # remove and return value
print(d)
d.setdefault('six', 6) # insert only if key missing
print(d)

# Utility
print(len(d))                # 5 — number of keys