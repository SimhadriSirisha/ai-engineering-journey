## Dict:
- its mutable data structures. eg: [exercises/example_1_dict_mutable.py](./exercises/example_1_dict_mutable.py)
- Python has method which similar to scala getOrElse() to access the key, if not then return default value. i.e `get(key name, default)`. eg: [exercises/example_2_access_dict_keys.py](./exercises/example_2_access_dict_keys.py)
- Dict & UserDict implements collections.abc.MutableMapping whereas set implements collections.abc.MutableSet & frozenSet implements collection.abc.Set
- users creating custom map mostly extend Dict or UserDict because Dict & UserDict already implement all the required methods, users can override the specific method if you want to change. The ABC gives you nothing pre-built, it's a blank contract.

**eg:**
- Almost nobody does this
```
class MyMap(collections.abc.MutableMapping):
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self): ...
    # You must implement ALL of these yourself from scratch
```
- People do this
```
class MyMap(dict):
    def __getitem__(self, key):
        # just override the one thing you want to change
        return super().__getitem__(key.lower())
```
- "ABCs are contracts for isinstance checks, not base classes for inheritance.": Because it helps in not breaking the code. 
```
# WITHOUT ABCs - fragile, breaks with custom mappings
def process(data):
    if isinstance(data, dict):   # ❌ only accepts dict, rejects other mappings
        ...

# WITH ABCs - robust, accepts anything dict-like
def process(data):
    if isinstance(data, collections.abc.Mapping):  # ✅ accepts dict, OrderedDict, 
        ...                                         # custom mappings, anything mapping-like
```
This function doesn't care if you pass a `dict`, an `OrderedDict`, a `UserDict`, or a custom config object. If it behaves like a Mapping, it works.
- Dict keys must be hashable because hashing converts a key to a slot number directly — O(1) lookup. Without hashing, Python would have to scan all keys linearly — O(n). The key itself must be hashable to generate that slot number reliably. 
    - How ? keys are objects, they implements `__hash__()`, so this hashable function generates one unique hash value(a memory address slot). Python uses this numnber to directly jump to get the value. So O(1)

### frozenset vs set
- set is mutable, not hashable so cannot be used as dict key.
- frozenset is immutable, hashable => can be used as dict key.
```
s = {1, 2, 3}         
fs = frozenset([1,2,3]) 

d = {}
d[fs] = "frozen"   # ✅ works
d[s] = "regular"   # ❌ TypeError: unhashable type: 'set'
``` 
frozenSet is the immutable version of set - similarly tuple is the immutable version of list.

## User-Defined Types — The Default Behavior
```
class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("Rex")
d2 = Dog("Rex")

hash(d1)  # works — uses id(d1), the memory address
hash(d2)  # works — uses id(d2), different address

d1 == d2  # False — different objects, even with same name
```
by default, both `__hash__` and `__eq__` use memory address — so two objects at different addresses are never equal, even with identical data.
Even if same name, they are different objects to solve this.
It can be written as : [exercises/example_4_user_defined_types.py](./exercises/example_4_user_defined_types.py). Here note this that both `__hash__` and `__eq__` methods are overrided together.
- If not overrided together, then it will produce error. Check this: [exercises/example_5_broken_dog.py](./exercises/example_5_broken_dog.py)

### Dict Declaration
- Different ways to declare a dict. [exercises/example_0_dict_declarations.py](./exercises/example_0_dict_declarations.py)
- If you observe clearly, here we have used `==` to check the content. **How does it worked ??** These build in types like dict, str, int override both `__eq__` & `__hash__` to check content.
- For dicts, `__eq__` is implemented to compare **contents**, not memory address. It checks:
    1. Do both dicts have the same number of keys?
    2. Does every key in a exist in b?
    3. Does every value match for every key?
All three true → Equal. order doesn't matter — dict equality is content-based
- `==` calls `__eq__` — for dicts this checks contents. is checks memory address.
- Mutable built-ins override `__eq__` but set `__hash__` = None. Immutable built-ins override both.

#### The Full Hashability Map
```
str        → ✅ hashable (immutable)
int        → ✅ hashable (immutable)
float      → ✅ hashable (immutable)
bytes      → ✅ hashable (immutable)
tuple      → ✅ only if ALL contents are hashable
frozenset  → ✅ always (contents must be hashable by definition)
list       → ❌ mutable
set        → ❌ mutable
dict       → ❌ mutable
```

#### Dict comprehension : 
refer [exercises/dict_comprehensions.py](./exercises/example_6_dict_comprehensions.py)

#### Dict methods (API mappings):
refer [exercises/dict_API.py](./exercises/example_7_dict_API_mappings.py)
- "API for mappings" = the methods any dict-like object must support. 
    The minimal contract is 3 methods:
    - __getitem__ — lets you do d[key]
    - __len__ — lets you do len(d)
    - __iter__ — lets you loop over keys). 
Everything else is derived from those 3 by the ABC.

## failure modes:
- In pyhon, everything is an object. when we call a method name without paranthesis (), for eg: `name.title` then we are actually referring the object and not calling it.
so when we do this `name.title` then it return object add without failing and when we call `name.title()` then title() called.

- In python, everything is an object, it creates, hash it and stores. This is a very big process. Even primitive int is also an object. Which has very much backend overhead. Because of this reason numPy introduced where numerical calculation happens with raw memory.

- Dict keys can't be mutable because:
Imagive list used as dict keys. As its list it can be changes and the hash value for the list will be different. Now, if python looks with new hash value, result u wont be able to see because dict stored at previous location.
```
key = [1, 2, 3]
d = {}
d[key] = "value"   # stored at slot hash([1,2,3]) = slot 99

key.append(4)      # key is now [1, 2, 3, 4]
                   # hash([1,2,3,4]) = slot 27 ← DIFFERENT SLOT

d[key]             # Python looks at slot 27. Nothing there. KeyError.
# The value is still at slot 99, now unreachable forever.
```
This way dict is corrupted. A value will exists but never found this is why dict keys can't be mutable.

- Tuple is immutable but it can't be used as dict keys because tuple can contain mutable objects like list. So the contents changed which implies the hash value also changes. So tuple cannot be hashable(hashable means who's hash value never gets changed). This brings an important point that `immutable != hashable` and can also be `Hashable = Immutable AND all contents are also hashable`
```
tt = (1, 2, (30, 40))   # tuple of tuples — all immutable
hash(tt)                 # ✅ works

tl = (1, 2, [30, 40])   # tuple containing a list — list is mutable
hash(tl)                 # ❌ TypeError
```


