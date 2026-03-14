### Python Basic
#### if-else condition
- The scope of a varible inside a if-else block is inside only & can't be accessed outside

### Fluent Python — Ch 2 (Predictions / Assumptions)

#### Sequence / MutableSequence ABCs (my assumption)

- ABCs(Abstract Base classes) like `Sequence` and `MutableSequence` are classes which have predefined functionalities with the help of dunder methods.
- With this they allow any built-in data structures without restricting to one, and also take care of type checking.
- So every `list`, `tuple`, etc are instances of `Sequence` / `MutableSequence` but not subclass (don’t inherit) from those ABCs.

#### Benefits I assumed

- **Flexibility**: If we use built-in data structures in annotations, we strictly restrict the API to use `list` only, whereas here we can give flexibility.
- **Extendability**: With ABCs we can extend and use it with different purpose by adding few more methods.
- **Ease of extension**: As they will have basic functionalities, extension becomes easy.

#### List comprehensions / generator expressions (my assumption)

- From the sentence “A quick way to build a sequence is using a list comprehension (if the target is a list) or a generator expression (for all other kinds of sequences)” I thought comprehensions are some classes: list comprehension is for lists and generator expression is for tuples.
- I also assumed they are mainly about how we apply some modification/functionalities on each element of the sequence.
- I understood the book’s style advice as: if the operation on each element is more than 2 lines, use a normal `for` loop; otherwise, use a comprehension.
- “a listcomp is meant to do one thing only: to build a new list.” — I took this as: because we write the expression inside `[]`, it will always return a list.  For other sequence types, I initially thought generator expressions directly create that specific sequence (e.g. tuple) instead of creating a generator that is then consumed by another constructor.

#### Cartesian product list comprehension (my assumption)

- I wrote the Cartesian product as:

  ```text
  t_shirts = [(colour, size) for colour in colours and size in sizes]
  ```

- I expected `and` to combine the two `for` parts so that both `colour` and `size` would be iterated, but this actually caused a `NameError` for `size`.
