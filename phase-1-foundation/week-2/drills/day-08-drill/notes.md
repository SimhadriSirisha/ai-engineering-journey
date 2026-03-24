## Dictionaries
Mthod fromKeys(keys: iterable, value) : This method creates a new dictionaries where the keys form from iterable and assign to each key the value.

**eg**:
    
    cards = {}.fromkeys(('red warrior', 'green elf'), 42)
    print(cards) # {'red warrior': 42, 'green elf': 42}

## String manipulation
1. S.format(*args, **kwargs) -> str
    - returns a formated version of S, using sabstitutions from args & kwargs. substitutions identified by curly braces ('{' & '}') and along with positional arguments.
    
    **eg**:
        
        "The values are {0} and {1}".format(value1, value2) 
        # here value1 will be substituted at pos 0 and value2 substituted at pos 1.

2. `:.{n}f` format spec
    - This tells how many decimals {n} after decimal should be printed.

    **eg**

        val = 1/3
        for p in [1, 4, 7]:
            print("{0:.{1}f}".format(val, p))
        
        o/p:
        0.3         # when p=1
        0.3333      # when p=4
        0.3333333   # when p=7
    
3. string.split(sep)
    - split the string with a sep and returns a list of strings

    **eg**:

        string = "Sausage Egg Cheese"
        words = string.split()
        words # ['Sausage', 'Egg', 'Cheese']

    - If want to split with different patterns then we can use regular expressions library `'re'`'s method `.compile(pattern: str)`.

    **eg**

        string = "the,rain;in,spain"
        pattern = re.compile(',|;') # Pattern is a Python regular expression pattern which matches ',' or ';'
        print(pattern.split(string)) # ['the', 'rain', 'in', 'spain']

4. raw string where excapes dont have any specific meaning, act as normal string character. `r'\n'`, basically we consider `\n` as new line but here when prefixed with `r` then the string consider as normal string with 2 characters. These are useful in filepath, regular expressions, URLs etc.

5. join string:

    Before we read about spliting a string with a sep string, simpilarly we have a `join` method to join the words.

    **eg**

        words = ["Now", "is", "the", "time"]
        print(' '.join(words)) # "Now is the time"

6. Capitalize() vs Title():
    
    capitalize() makes the first character of the string to upper case where as title() makes the first character of each word in string to upper case.

    **eg**

        'guido van rossum'.capitalize()     # 'Guido van rossum'
        'guido van rossum'.title()          # 'Guido Van Rossum'

## Tuples
- These are all identical — just grouping expressions

        x = (5)
        x = ((5))
        x = (((5))) # x is int every time

- The comma is the tuple constructor

        x = (5,)      # tuple with one element
        x = 5,        # also a tuple — parentheses optional!
        x = (5, 6)    # tuple with two elements
        x = 5, 6      # also a tuple

- tuple("Surprise!") -> ('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!')

## Methods
1. If we call methods with wrong arguments then its not syntax issue, its runtime error.

        def test(a, b):
            return a+b

        test(1, 2, 3) # fails at runtime

2. *args & *kwargs : args takes tuple where as kwargs takes dict.

        def example(*args, **kwargs):
            print(args)    # tuple  — positional arguments
            print(kwargs)  # dict   — keyword arguments

        example(1, 2, 3, name='John', age=30)
        # args   = (1, 2, 3)
        # kwargs = {'name': 'John', 'age': 30}

    - passing in two ways :

            def show(*args):
                print(args)

            show([1, 2, 3])    # prints ([1, 2, 3],) — a tuple containing a list
            show(*[1, 2, 3])   # prints (1, 2, 3,)  — unpacked, each element is an arg

3. function call with `.self` : When called with `.self` it always check the class method without checking this flow `LEGB`.
- `L`: local scope (inside current function)
- `E`: enclosing scope (outer function if nested)
- `G`: global scope (module level)
- `B`: Built-in scope (len, print)

4. In python every this is object, so even functions are object which can be assigned, passed as parameter and returned

5. `pass` in the method does nothing, its just one successful line.

6. No indentation is required for one line statement bodies.

7. documentation of a method can be viewed with `.__doc__`. `__doc__` is a **string**. Python stores the string literal as the first statement of the function as its docstring & stores in `__doc__`

        def doc():
            "This is the documentation" # stored in __doc__
            pass

        print(doc.__doc__) # prints "This is the documentation"

8. There are 3 levels of access in Python. 
    
            class Dog:
                def name(self):         # public — anyone can access
                    return "Fido"
                
                def _tail(self):        # "private" — convention only, still accessible
                    return "wagging"
                
                def __password(self):   # name-mangled — actively harder to access
                    return "password"

- Here, `_` before any method says that its private but doesn't enforces us to not to use. It just informs the developer that tail method is a private. If dev wants to access then can call as `dog._tail()`

- `name-mangled` : python renames these methods with double underscore `__` to `_[classname][Methodname]`. In the above example case it is `_Dog__password`. If wanted to access then we have to access as `dog._Dog__password`. We need this because it prevents from accidental overriding of parent class methods.

    **eg**

            class Dog:
                def __password(self):
                    return "Dog Pswd"
            
            class GuideDog:
                def __password(self):
                    return "Guide Pswd"