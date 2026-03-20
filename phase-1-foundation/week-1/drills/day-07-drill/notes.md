# Lists
- In list slicing, when start and end are same then it returns an empty list [] because slicing extracts elements starting from the start index (inclusive) up to, but not including, the stop index which contradicts so returns []
- range(n) will return range type and to get the list out of it then we will use list(range(start, stop[, step])). If start not given, then the start always starts from 0.
```
list(range(4)) # [0, 1, 2, 3]
list(range(1, 4)) # [1, 2, 3]
```
- There is `pop` but no `push`, because acc. to python there should be only one method for one operation, as we have append, so no need to have `push`.
- `Why poping from the left hand side of a list is inefficient and efficient to use is collection.deque?` : 
    - my prediction: if you pop from left hand side, you again have to shift the places of all the elements to left. It takes O(n). Whereas deque use two pointers `front` and `rear`, if removed from front, front pointer only moves. So its time complexity is O(1)
    - Actual: I was partially wrong as deque i.e. deque (double-ended queue) is implemented as a doubly linked list of fixed-size blocks. So we will be knowing front and back element of each node. so we can move the head pointer to next. other points is same from my prediction.
- Lists can also unpack same as tuple.
- List is mutable, tuple are not and collections.abc.Sequence is neither — it's a blueprint/ type hint thats it.
