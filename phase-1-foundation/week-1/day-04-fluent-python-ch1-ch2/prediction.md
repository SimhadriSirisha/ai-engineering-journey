### Python Basics

#### About Slices

- Slices will generate error when we try to access wrong index.

  **eg:**

  ```text
  my_foods = ['pizza', 'falafel', 'carrot cake']
  friend_foods = my_foods[2:4] // error
  ```

- in slicing, when referencing from backwords / forwards, index will start from 0 from forward and from backward starts as -0, -1, so on

#### About list assignment

- What this line does 'friend_foods = my_foods' ?

  **eg:**

  ```text
  my_foods = [pizza', 'falafel', 'carrot cake']
  ```

  copies the my_foods list to friends_foods

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

which one is better code practice ? code 1, because it assigned to a variable and then used that variable

### Python Datamodels
