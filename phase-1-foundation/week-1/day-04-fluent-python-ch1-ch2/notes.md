### Python Basics

#### About Slices

- In Python, slicing never raises an error when indices are out of range. It just returns the part of the sequence that exists within the valid indices.

  **eg:**

  ```text
  my_foods = ['pizza', 'falafel', 'carrot cake']
  friend_foods = my_foods[2:4] // o/p = ['carrot cake']
  my_foods = ['pizza', 'falafel', 'carrot cake']
  friend_foods = my_foods[3:4] // o/p = []
  ```

- *in slicing, when referencing from backwords / forwards, index will start from 0 if forward & -0,-1 if backwards* : Wrong

  - from forward, indexing starts from 0
  - from backword, indexing start from -1

  **eg:**

  ```text
  players = ['charles', 'martina', 'michael', 'florence', 'eli']
  print(players[-3:]) // o/p: ['michael', 'florence', 'eli']
  ```

#### About list assignment

- What this line does 'friend_foods = my_foods' ?

  **eg:**

  ```text
  my_foods = [pizza', 'falafel', 'carrot cake']
  ```

  *copies the my_foods list to friends_foods* - **Wrong**

  both points to same list reference, so even if you append different values using different variable, it impacts the same list as referencing same list.

  **eg:**

  ```text
  my_foods.append('cannoli')
  friend_foods.append('ice cream')
  print(my_foods) // [pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
  print(friend_foods) // [pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
  ```

  But to create copy, use 'friend_foods = my_foods.copy()'

#### About best practices

**code 1:**

```text
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
```

**code 2:**

```text
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
```

which one is better code practice ? code 1, because it assigned to a variable and then used that variable -> **Wrong**

code 2, is best practice and clean looking, here the variable is used only once so can be used directly without usage of any variable, and the statement `value**2` is very clear no need of assignment. If the statement is very big, then assigning to a varible gives some meaning to the statement.

Most Pythonic option for this task is : `squares = [value**2 for value in range(1,11)]`

### Python Datamodels
#### shuffling
for shuffling we need a new dunder method for random.shuffle(x) to execute because shuffling expects to do something like `seq[i], seq[j] = seq[j], seq[i]` and this assignment will be success if the sequence is mutable. So, The FrenchDeck object’s public sequence interface is immutable (you can’t change it via deck[i] = ...), but its internal data member _cards is mutable, so the object itself can still be mutated if you bypass the interface and touch _cards directly. The special dunder method is `__setitem__`.

#### other special dunder method:
- `__repr__(self)`: string representation of object. Very much used for debugging.
  other form of equivalent representation of `'Vector(%r, %r)' % (self.x, self.y)` is :
  ```
    f"Vector({self.x!r}, {self.y!r})"
  ```

### Python DataStructures
#### Array of Sequences :
- different types of sequences:
  - Group 1:
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