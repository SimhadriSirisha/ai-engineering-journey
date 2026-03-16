## AboutNone — Reflections

### What surprised me
In python everything is a object, even a single function is a object. So, even `None` is a object.
`isinstance(None, object)   # → True`

### None vs null — key difference
None is a real object. Not a pointer. Not an absence.
NoneType inherits from object.

### When to use `is None` vs `== None`
`is` checks the identity whereas `==` checks the equality
- `is` checks whether they have same memory
- `==` checks whether they have same value

**eg**
```
a = [1, 2, 3]
b = [1, 2, 3]

a == b    # → True
a is b    # → False

a = [1, 2, 3]
a = b

a is b    # → True
a == b    # → True
```

### AttributeError — when does it happen
When we try to access something which is not defined in the object.

### Silent failure I now understand
None & 0 both are different. 
but bool(None) & bool(0), gives same result i.e. false. But 0 is a valid result.

Here it silently fails:
```
result = get_prediction()   # returns None on failure

if not result:              # True for None, 0, False, [], {}
    print("no result")      # fires for ALL of these
```

