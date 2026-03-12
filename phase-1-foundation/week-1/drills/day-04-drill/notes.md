1. self.assertTrue(x) # x must be true
2. self.assertTrue(x, 'msg') # x must be true, else exception raised with this msg
3. self.assertEqual(a,b) # a must be equal to b
4. assert x == y # raw python assert
5. self.assertTrue(x == y) # x == y should be true, assertTrue can take expressions
6. `__class__` : used to return the class name.
    **eg:**
    ```text
    >>> 'Hello'.__class__
    <class 'str'>
    ```

    Here, the assertion should be done as `self.assertEqual(str, 'Hello'.__class__)` and **not** `self.assertEqual(<class 'str'>, 'Hello'.__class__)`. During assertion it always checks for `__name__`

#### failure modes:
The most dangerous thing about assert in Python: asserts are disabled when Python runs with the -O (optimize) flag. Production code that relies on assert for input validation is a silent bug.