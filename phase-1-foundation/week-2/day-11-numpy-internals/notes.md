# NumPy Internals
We know that use C compiled function execution numPy is faster but **HOW ?** 
There are 2 strategies i.e. **Vectorization** & **Broadcasting**

## Vectorization
- When operation on array is of same shape then this strategy used where entire array execution happens in shot.
- This eliminates the usage of Loop.
- CPU can use SMID, process multiple elements in literally one CPU instruction 

    **eg**

        # NOT vectorized — Python processes one by one
        result = []
        for x in data:
            result.append(x * 2)    # Python touches each element

        # Vectorized — C processes all at once
        result = arr * 2            # One C function call, entire array

## Broadcasting 
- When operation on array is of different shape(i.e. different dimensions) then this stategy used
- The resulted array will have dimension with largest size.

    **eg**

        a = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])   # shape (3, 3)

        b = np.array([10, 20, 30]) # shape (3,) -> here numPy pads 1 to the left

        result = a + b
        # Adds b to every row of a
        # b is NOT copied into a (3,3) array first
        # result shape will (3, 3)

- C function uses stride tricks to avoid copying
- no unnecessary memory copies.

### Broadcasting rules :
Dimension comparision happens from right to left. 
If the dimension is either :
- equal or,
- one of them is 1,

then broadcasting is possible.

For each dimension pair (right to left):

        Are they equal?
           ↙       ↘
         YES        NO
          ✅    Is one of them 1?
                   ↙       ↘
                 YES         NO
                  ✅       ValueError ❌
               (stretch     (incompatible
               the 1 to      shapes)
               match other)

   **eg**

    # ✅ COMPATIBLE
    (3, 4) + (3, 4)  → equal dims          → (3, 4)
    (3, 4) + (1, 4)  → 3vs1, stretch       → (3, 4)
    (3, 4) + (3, 1)  → 4vs1, stretch       → (3, 4)
    (3, 4) + (4,)    → pad→(1,4), stretch  → (3, 4)
    (3, 4) + (1, 1)  → both 1, stretch     → (3, 4)

    # ❌ INCOMPATIBLE
    (3, 4) + (3, 3)  → 4vs3, neither 1              → ValueError
    (3, 4) + (2, 4)  → 3vs2, neither 1              → ValueError
    (4, 3) + (4,)    → pad→(1, 4) → 3vs4, neither 1 → ValueError

When dimension is missing, then numpy pads 1 to the left always and stretches. Because when an array is (4,) this means 4 elements in single row. So 1 should be padded to the left.

# Benchmark 
[Benchmark Code](phase-1-foundation/week-2/day-11-numpy-internals/exercises/benchmark.py)


# The Complete Mental Modal

1. Array restriction : numPy always uses contiguous memory with elements of same type.
2. ufunc lookUp : Depending on the operation numPy calls respective C function by checking dType.
3. Boundary crossing : Python passes raw memory pointers to C. Only passes addresses
4. Inside C : Either vectorization or broadcasting or both depending on shape.
5. Result back : C writes to output memory and python wraps it as a new ndarray
