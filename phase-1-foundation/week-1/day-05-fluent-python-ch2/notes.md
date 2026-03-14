### Python Basic
#### if-else condition
- The scope of a varible inside a if-else block is not only inside& it can be accessed outside
- we can have if-elif conditions without else block, because else block is not mandatory
- string equal checks possible with '==' or '!='
- In Python, empty containers are falsy by default:
```
[] → falsy
{} → falsy
"" → falsy
None → falsy
```
So we never need `.isEmpty()` like in Scala. Just use `if x:` or `if not x:` directly.
This is the Python data model working for you — the same dunder system from Fluent Python Ch 1. The __bool__ and __len__ methods control truthiness. If __len__ returns 0, Python treats the object as falsy automatically.

### Python DataStructures
#### Array of Sequences :
- different types of sequences can groupes in 2 different ways:
- Group with way 1:
    - Container Sequences (list, tuple & collections.deque) : Hold items/objects of different types.
      - key idea: They store references to objects, not raw data
    **eg**
    ```
      items = [1, "hello", 30.0, [10,20]] #list
      t = (1, "a", [2,3]) #tuple - immutable
      dq = deque([1, 'x', 3.5])
    ```
    - Flat Sequences (str, bytes, bytearray, array.array, memoryview) : store sequences of raw values of same type.
      - key idea: no python object per item overhead
    **eg**
    ```
      s = "hello"
      print(s[0]) # 'h'
    ```
    ```
      # bytes: (immutable)
      b = b"ABC"
      list(b) # [65, 66, 67]
    ```
    ```
      # bytearray (mutable)
      ba = bytearray(b"ABC")
      ba[0] = 97 # now ba is b"aBC"
    ```
- Group with way 2:
    - Mutable sequences (list, collections.deque, bytearray, array.array(numeric typed array), memoryview)
    - Immutable sequences (tuple, str, bytes)

#### Tuples: two roles (Fluent Python)

Tuples are immutable but are used in two different ways:

1. **As an immutable list**  
   You only need a fixed sequence that can’t be changed. The **number** of items and their **order** may or may not matter—it depends on context (e.g. “a list of tags”, “something to iterate”).

2. **As records (no field names)**  
   Each **position** is one field; **position gives the meaning**. The number of items is usually **fixed** and **order is always vital** (e.g. position 0 = city, 1 = year).

**How the book’s sentence maps to the two roles**

- *“If you think of a tuple just as an **immutable list**, the quantity and the order of the items **may or may not** be important, depending on the context.”*  
  → **Role 1:** You’re not treating each index as a named field; it’s just “a sequence”.

- *“When using a tuple as a **collection of fields**, the number of items is often **fixed** and their order is **always vital**.”*  
  → **Role 2:** Each index is a specific “column” (e.g. country, id); swapping two values would change the meaning.

**Book example — each tuple as record**

- **`lax_coordinates = (33.9425, -118.408056)`**  
  **Record:** position 0 = latitude, position 1 = longitude. Two fields; order vital (swap them and the point is wrong).

- **`city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)`**  
  **Record:** exactly 5 fields—city, year, population, change, area. Unpacking by position only works because order is fixed.

- **`traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]`**  
  Each element is a **record** of 2 fields: (country_code, passport_id). So when you write  
  **`for country, _ in traveler_ids`** you’re using the tuple as a record: first field = country, second = id (ignored with `_`).  
  **`print('%s/%s' % passport)`** — same idea: position 0 and 1 are fixed meanings (country, id).

So in this example **every tuple is used as a record**: fixed number of fields, order matters. The "immutable list" role would be when you only care that it's a sequence (e.g. `for x in (1, 2, 3)` or "keep these three values together") and you don't rely on "index 0 = this, index 1 = that".

**Same data, Role 1 (immutable list):** Use the same tuples but do not treat position as "field meaning"—just iterate or use indices. E.g. `lax_coordinates`: `for x in lax_coordinates: print(x)` or `sum(lax_coordinates)` (no "index 0 = lat"); `traveler_ids`: `for passport in traveler_ids: print(passport)` without unpacking, or `traveler_ids[0][1]` (just "second item"). Role 2 = unpack by meaning (`country, id = passport`); Role 1 = use as plain sequence (`p[0]`, `p[1]` or iterate).

#### Sequence / MutableSequence ABCs (why they matter)

**Book line:** built-in concrete sequences don’t actually subclass `Sequence` / `MutableSequence`, but the ABCs are still useful as a formalization of what functionality to expect from a “full-featured” sequence type.

- **What an ABC is here**
  - `collections.abc.Sequence` and `collections.abc.MutableSequence` are *abstract base classes* that define a **contract** (expected methods/behavior) for sequence-like types.
  - They may provide **some default methods**, but their main value is the **formal interface** they represent.

- **Built-ins don’t inherit from these ABCs**
  - `list`, `tuple`, `str`, etc are implemented in C and **do not literally inherit** from these ABC classes.
  - So “subclass” checks can be false:

    ```text
    issubclass(list, MutableSequence)   # False
    issubclass(tuple, Sequence)         # False
    ```

- **But many built-ins are “virtual instances” (behavior-based)**
  - Even without inheritance, ABCs can recognize compatible types for `isinstance`:

    ```text
    isinstance([], MutableSequence)     # True (typical)
    isinstance((), Sequence)            # True (typical)
    ```

- **How ABCs help in type checking + API docs**
  - They let you type your API by **capability**, not by a single concrete type.
  - Example: a function that only needs indexing/`len()` should accept a `Sequence`, not only a `list`:

    ```text
    def first(xs: Sequence[int]) -> int:
        return xs[0]
    ```

  - Type checkers can then catch wrong assumptions:
    - `Sequence` does **not** promise mutation (no `.append`), so a checker flags code that assumes mutability.
    - If mutation is required, annotate `MutableSequence` instead.

- **Actual Benefits**
  - They gives a contract, if any class inherits those ABCs, from these, we dont have implement extra methods, we will be getting more methods free and we can look after the actual requirement methods

#### List comprehensions and generator expressions

- **List comprehensions**
  - Syntax: `[expr for item in iterable if condition]`.
  - Always produce a **list** because of the `[]`.
  - Intended to do **one main thing**: build a new list, usually as a clear, single-expression transformation/filter.
  - Example:

    ```text
    squares = [x * x for x in range(5)]        # [0, 1, 4, 9, 16]
    evens = [x for x in range(10) if x % 2==0] # [0, 2, 4, 6, 8]
    ```

- **Generator expressions**
  - Syntax: `(expr for item in iterable if condition)`.
  - Produce a **generator** (lazy iterator), *not* a tuple directly.
  - Often used to feed other constructors that accept any iterable:

    ```text
    t = tuple(x * x for x in range(5))   # tuple built from a generator
    s = set(x * x for x in range(5))     # set built from a generator
    ```

- **Style guidance**
  - If the per-item logic is **simple and fits comfortably on one line**, a comprehension is usually clearer and more idiomatic.
  - If the logic per element needs **multiple steps / multiple lines**, prefer a regular `for` loop for readability.

#### Example: `map`, `filter`, `lambda` for non-ASCII code points

```text
symbols = "$¢£¥€¤"
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
```

- `map(ord, symbols)` turns each character into its Unicode code point (integer).
- `filter(lambda c: c > 127, ...)` keeps only those code points **greater than 127** (i.e., non-ASCII characters).
- `list(...)` materializes the filtered integers into a list.

- The same logic using a **list comprehension** (what the book means by “listcomps do everything `map` and `filter` do, without the contortions of `lambda`”):

  ```text
  beyond_ascii = [ord(ch) for ch in symbols if ord(ch) > 127]
  ```

  This both **maps** (via `ord(ch)`) and **filters** (via `if ord(ch) > 127`) in a single, readable expression, without needing an explicit `lambda`.

#### Cartesian product list comprehension

Given:

```text
colours = ['black', 'white']
sizes = ['s', 'm', 'l']
```

- The incorrect attempt:

  ```text
  t_shirts = [(colour, size) for colour in colours and size in sizes]
  ```

  fails because `for colour in colours and size in sizes` is parsed as
  `for colour in (colours and size in sizes)`, which references `size` before it exists.

- The correct Cartesian product comprehension uses **two `for` clauses**:

  ```text
  t_shirts = [(colour, size) for colour in colours for size in sizes]
  ```

  This iterates `colour` over `colours`, and for each `colour`, iterates `size` over `sizes`, producing all `(colour, size)` pairs.

### Generator Comprehension

- Generators are similar to list comprehension but use parentheses instead of square brackets.

#### Generator expression vs list comp: why gen exp saves memory (Cartesian product)

- **List comprehension** builds the **entire sequence in memory** before you use it:

  ```text
  colours = ['black', 'white']   # e.g. 1000 items
  sizes = ['s', 'm', 'l']       # e.g. 1000 items
  t_shirts = [(c, s) for c in colours for s in sizes]   # list: 1M tuples in RAM
  for t in t_shirts:
      print(t)
  ```

  All 1,000,000 tuples exist in memory at once.

- **Generator expression** produces **one item at a time** when the `for` loop asks for the next value; it does not build a list:

  ```text
  t_shirts = ((c, s) for c in colours for s in sizes)   # generator object
  for t in t_shirts:
      print(t)
  ```

  Only the current tuple and a small amount of iterator state are in memory. So the “six-item list of T-shirts” (or the million-item list) is **never built**—the gen exp **feeds the loop one item at a time**.

- **Takeaway:** Use a **list comp** when you need the full sequence (random access, multiple passes, or to store it). Use a **generator expression** when you only iterate once (e.g. feeding a `for` loop or a constructor like `tuple(...)`); that avoids holding the whole result in memory.

- **When to use which — examples**

  **Use a list when you need the full sequence:**

  - **Indexing:** first item, last item, or any position.

    ```text
    squares = [x * x for x in range(100)]
    print(squares[0], squares[-1])   # need list: indexing
    ```

  - **Multiple passes:** iterate more than once.

    ```text
    items = [f(x) for x in data]
    total = sum(items)
    count = len(items)   # second use of same sequence
    ```

  - **Storing:** you keep the result for later.

    ```text
    cache = [expensive(x) for x in inputs]
    return cache
    ```

  **Use a generator when you only consume once:**

  - **Single pass:** one loop, or one function that consumes the iterator.

    ```text
    total = sum(x * x for x in range(100))        # one pass, no list
    t = tuple(n * 2 for n in data)                # one pass into tuple
    for pair in ((c, s) for c in colours for s in sizes):
        print(pair)   # one pass; never build full list
    ```

  **Runnable validation (same data, list vs generator):**  
  Run `example2-3_list_vs_genexp.py`. It uses the same sequence (squares of 1..5) as both a list and a generator:
  - **List:** `sum(squares_list)` twice → both **55**; `squares_list[0]` → **1** (indexing works).
  - **Generator:** `sum(squares_gen)` first → **55**; second `sum(squares_gen)` → **0** (exhausted after one pass). No indexing (generators are not subscriptable).
  So list supports multiple passes and indexing; generator is one-shot.
  - This is a production bug. A generator passed to two consumers gives wrong results with no error.

