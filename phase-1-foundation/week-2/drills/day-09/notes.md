## True & False
1. When checked with empty primitive data types like dict, list, tuple, str, etc are all considered as false only.

**eg**:
        [], (), {}, "", set() -> all are falsy

## Sets
1. set always takes single parameter. 
**eg**: `set(1,2,3)` this is wrong where as `set([1, 2, 3])` this is correct.

2. If `{1}` is Set then empty Set is not `{}` rather it is `set()`. Why this inconsistency because dict was introduced first and then set introduced. So any object with only values and no colon i.e. {1, 2, 3} then its set, If the object key:value pair with colon then its dict.

        # Python asks: "does it have colons?"
        {1, 2}      # no colons  → set
        {1: 'a'}    # colons     → dict
        {}          # no colons, no values → Python chose dict (historical reason)
        set()       # only way to make empty set

3. set iterates through whatever we give it.

    **eg**:
        
        # These are all identical in behavior
        set('12345')        # iterates string → each char becomes element
        set(['1','2','3','4','5'])  # iterates list → each item becomes element
        set(('1','2','3'))  # iterates tuple → each item becomes element

- set follows 3 steps:
    - step 1: iterate through each element
    - step 2: removed duplicate
    - step 3: result

    **eg**:

        a = set('aabbcc')
        b = set(['aabbcc'])
        c = set(['a','a','b','b','c','c'])
        d = { x for x in 'aabbbcccc'} # as there is no colon so `d` is set.

        print(len(a))   # 3 — {'a','b','c'} duplicates removed
        print(len(b))   # 1 — {'aabbcc'} one string
        print(len(c))   # 3 — {'a','b','c'} duplicates removed
        print(len(d))   # 3 - {'a', 'b', 'c'}

4. set can have arithmatic operators

5. set can have comparision operators 

        a <= b    # a is subset of b (all a elements exist in b)
        a <  b    # a is proper subset (subset AND a != b)
        a >= b    # a is superset of b (all b elements exist in a)
        a >  b    # a is proper superset
        a == b    # identical elements

## Exception:
1. MRO — Method Resolution Order: It is the order Python follows to look up methods when you call something on an object. `.mro()` shows you exactly which order Python searches classes.
    ```
    class A:
        def hello(self):
            return "A"

    class B(A):
        def hello(self):
            return "B"

    class C(A):
        def hello(self):
            return "C"

    class D(B, C):  # inherits from both B and C
        pass

    print(D.mro())
    # [D, B, C, A, object]

    d = D()
    d.hello()   # returns "B" — follows MRO order
    ```
This order always ends with `object` because every class implicitly inherits from object. This gives all classes built-in methods like `__str__`, `__repr__`, `__init__` for free.

2. mro of exception is : `[<class 'RuntimeError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]`

3. Try/else/final :

        try:
            # attempt something risky
        except RuntimeError:
            # runs ONLY if RuntimeError was raised
        else:
            # runs ONLY if NO exception was raised
        finally:
            # runs ALWAYS (optional, not shown here)

    `Try-else` block is mostly unused pattern, which doesn't has any specific reason. Maybe it seperates a specific lines for catching error with proper documentation.

## Iteration:
1. iterators are of special type. They are objects which can used only once. Why once ?
```
it = iter(range(1,6))

for num in it:
    print(num)

for num in it:
    print(num)   # ❌ Nothing prints
```
but instead of iter(), if only used directly range(), we can do the for loop multiple times.
```
it = range(1,6)

for num in it:
    print(num)

for num in it:
    print(num)   # ✅ Works again
```
when done `for num in range(1, 6)`, python internally converts `range(1, 6)` to `iter(range(1,6))` everytime.

one benefit we can get from iter() is when we want to check the values manually using `next()` which can't be done using range()
```
it = iter(range(1,4))
print(next(it))  # 1
print(next(it))  # 2
```
If the **iteration with next()** exceeds the size of iterator the return an exception `storIteration`.

2. `map()` takes 2 or more parameters : function and one or more iterables (on which iterator can be applied). For each element in the iterable it applies the function and generates a map object which is again an iterator not a list. As its iterator, u need to use next() to get the required elements one by one. It is one type of memory optimizer because map is a lazy. It doesn't generate all the values upfront as list, it generates only when needed. map is an iterator because it implements `__iter()__` & `__next()__`.
    ```
    list(map(self.add_ten, seq)) # forces everything to generate at a time
    map(self.add_ten, seq) # stores nothing & processed on demand
    ```

3. `filter()` takes 2 or more parameters same as map : function and one or more iterables. It returns an filter object which is iterator. It returns items of iterables which true for the given function. If funtion is None then it returns items which are true.
        def is_even(item):
            return (item%2) == 0

        seq = [1, 2, 3, 4, 5, 6]
        even_numbers = list()

        for item in filter(is_even, seq):
            even_numbers.append(item) 

4. `reduce()` takes function with 2 arguments - accumulator and real parameter, because it applies the function cumulatively across the iterable. It is present inside the module `functools`.

        def func(accumulator, current):
        ...
    How it works :

        result = func(func(func(a, b), c), d)
    
    When function takes only 1 parameter or 3 then gives `typeError`

        def f(x):
            return x

        reduce(f, [1,2,3])  # ❌ TypeError

        def f(a, b, c):
            return a + b + c

        reduce(f, [1,2,3])  # ❌ TypeError
    
    we can extend these function to make into 2 parameters useing `lambda`

        reduce(lambda acc, x: acc + x + 1, seq)

    with initializer, acc intitalized with initial value and then the function applied. So it returns a single value.

5. strip() cleans a string by removing whitespace (or specified characters) from both ends, but leaves the middle unchanged.

## Generators
A function with yield is generator function. Instead of computing everything at once and returning everything at a time. It produces one value at a time and produces the next one when requested.
```
def simple_generator_method():
    yield 'peanut'    # pause here, give 'peanut'
    yield 'butter'    # pause here, give 'butter'
    yield 'and'       # pause here, give 'and'
    yield 'jelly'     # pause here, give 'jelly'
```

Why this matters ? In ML, if used regumar function to load every image to RAM, then RAM will explode. To avoide this we used generator function and load the image when needed. PyTorch's `DataLoader` uses this pattern internally.

```
def counter():
    yield 1
    yield 2
    yield 3

gen = counter()

print(next(gen)) # 1
print(next(gen)) # 2
print(list(gen)) # [3]
print(list(gen)) # []
```

Execution of this function :
```
def sum_it(self, seq):
        value = 0
        for num in seq:
            value += num
            yield value
```
```
value = 0                    # initialised once

# Iteration 1
num = 1
value = 0 + 1 = 1
yield 1                      # pauses here, gives 1 to caller

# Iteration 2 — resumes from yield
num = 2
value = 1 + 2 = 3
yield 3                      # pauses here, gives 3 to caller

# Iteration 3 — resumes from yield
num = 3
value = 3 + 3 = 6
yield 6                      # pauses here, gives 6 to caller

# Iteration 4 — resumes from yield
num = 4
value = 6 + 4 = 10
yield 10                     # pauses here, gives 10 to caller

# Loop ends — StopIteration raised automatically
```

The Key Insight

`value` is **not reset between yields.** The entire local state of the function is frozen when it pauses and restored when it resumes.

Input:  [1, 2, 3, 4]

Output: [1, 3, 6, 10]   ← running total, not individual values

## Coroutines via Enhanced Generators
Coroutines are the functions which pause the execution, remember where it left and resume the execution. This is something like async/await.

These are useful when multiple things needs to be happened at the same time without having the overhead of threads and OS interuption. With single thread, cooroutines can decide where to pause and others continue the work once the pause condition satisfied, the coroutine will resume. 

but for our event driven programming, asynchronous I/O needs function to recieve till then function has to wait.

With the help of corouting, python can support performing asyncronous operations without needing to have frequent callbacks and any intensive resources like threads.

**eg**:

application takes request and hit db where db takes 100ns, then without couroutine, we will be taking the req and send the request to db, wait for db response and then proceed with the task complete and move to next function. Which cause a great delay, with coroutine when the task waiting for db response we could use cpu for taking request.

`Generators` are not complete coroutine, because they can pause to return the value but not to recieve the values or exception from outside world. And also they are not allowed to pause in the try/finally blocks. Due to which here comes the coroutine support with small syntax changes and addition of few methods.

*Using `yield` as expression instead of statement (The inverted function call):*

In normal functions, we only pass the parameter and it returns a value where as the `function with yield as expressions` returns the value to the caller and then caller sends a parameter using `.send(<value>)` and the function will takes and uses the function.

        name = yield "ready"
        
    This one line does two things:

    Sends "ready" outward to the caller (pauses the generator)
    Receives whatever the caller sends back, stored in name

    A normal function is one-way: arguments go in, return value comes out. yield inverts this — "ready" goes out, and a value comes back in at the same point. That's why PEP 342 calls it an "inverted function call."

    *How to actually use it*
        
        greeter():
            name = yield "ready"
            print(f"Hello, {name}")

        g = greeter()
        next(g)          # primes — runs body until yield, pauses there
        g.send("Alice")  # sends "Alice" in → name = "Alice" → prints Hello, Alice

    *The priming gotcha*

    When you create a coroutine with g = greeter(), the function body hasn't run at all. There's no yield waiting to receive anything yet.
        
    If you call g.send("Alice") immediately → TypeError.
        
    You must prime it first with next(g) or g.send(None) — this runs the body forward until it parks at the first yield. Only then is there a yield expression ready to receive.
    
    Fix in production — use a decorator to auto-prime:
        
        prime(fn):
            def wrapper(*args, **kwargs):
                g = fn(*args, **kwargs)
                next(g)
                return g
            return wrapper

    *The mental models to remember*
        
    ConceptMental modelyield as expressionWalkie-talkie — first switch on (next), then transmit (send)PrimingThe body is frozen at start. next() runs it to the first yieldWhy async/await worksThe event loop auto-primes coroutines — you never see this

    *The progression*

        yield (statement)     → one-way: sends values out only
        yield (expression)    → two-way: sends out + receives in
        coroutines            → built on this two-way yield
        async/await           → syntactic sugar over coroutines

