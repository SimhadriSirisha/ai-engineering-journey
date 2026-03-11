## What is ** in python ?
- its the power
- eg: 2**3 = (2)^3 = 8

## Python Data model:
Here, data model explains about class and object creation in python. DataStructures likes list, array, tupple etc. 
The dunder is what Python calls internally when you write my_collection[key]. You don't call `__getitem__` directly — you write my_collection[key] and Python calls `__getitem__` for you. 

### Dunder methods
refer: [exercise/example1-1.py](./exercise/example1-1.py)

- Here, NamedTuple is tuple class named as Card with 2 data members names as 'rank', 'suit'
- The use of Dunder methods is to provide integration with python syntac + standard protocols
- Python’s core containers like list, dict, and str implement many special (“dunder”) methods.
Built‑in functions and syntax such as len(x) and x[i] work by calling these methods internally, for example len(x) → x.`__len__` and x[i] → x.`__getitem__`(i).
If we implement the corresponding dunder methods on our own classes, those same built‑in operations will call our methods instead, so our objects can behave like the built‑in data structures while operating on our own internal state. This is not a concept of inheritance anything, This is duck typing: Python doesn't check what type the object is, only whether it has the right method. The way list build-in functions call their dunder method similarly for user-defined object if that dunder present then python calls the respective dunder method to built-in functions and syntax
- *How python know which dunder method to call ?* Python knows because len() is hardcoded in CPython's source to look for and call __len__. Every built-in operation has a corresponding hardcoded dunder. This is the protocol — a convention baked into the language runtime itself.
- *How random.choice() worked, even if there is no dunder method?* choice is a function which internally use len(), x[i], if len() & deck[i] worked then choice() will get an random value. So, random.choice doesn’t care whether it’s a list, your class, or something else; it only needs “an object that supports len() and []".
- *How the deck become iterable?* It is a Python's protocol that an Object is iterable if: it has `__iter__` dunder method, or it has `__getitem__` that accepts indexes 0,1,2,3,.... goes till it raises IndexError and then stops. This was kept for backword compatibility of older protocols.

*Advantages*:
- We don’t have to memorize separate methods for each type of object. eg: for finding length, I should .size() or .len()
- We can reuse existing built‑in operations instead of inventing new methods for the same purpose.