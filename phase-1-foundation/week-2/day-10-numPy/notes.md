# NumPy
- NumPy is a C-compiled array commutation engine. Every python code we write is a wrapper and is executed in C, so that's why faster.
- Any operation that touches array data has a C function that takes the entire array as input and processes it at machine speed.

**What will happen for operation that touches other data structure ?**

NumPy library always works on array/ndarray, a contiguous memory with same types because NumPy internally calls C for execution, and C cannot work on arrays with different types because different types stores scattered in memory and C connot find.

** eg **
    
    arr = np.array([1, 2, 3, 4])
    # C function knows exactly where each element is

    lst = [1, "hello", 3.14, True]
    # Python list — C cannot do this as elements as scattered

**Are these C function parameters are dynamic ?**

No, But better than dynamic. Because numPu has ufuncs (Universal functions) i.e there is a specific function for each combination of types. So NumPy calls specific function for specific type combination. No dynamic resolution. No flexibility overhead.
`Just: check types → find right function → pass memory → done.`

In Spark, when you call .filter() on an RDD of integers vs an RDD of strings — Spark uses different execution paths internally for different types.

**These can be chances of infinite combinations then how its handled ?**

- NumPy directly supports few core types and not work for all this will reduce a bit. 
- And if pass a combination that has no pre-compiled function, NumPy promotes types upward to the nearest supported combination. `int8 → int16 → int32 → int64 → float32 → float64`
- NumPy does NOT have a special C function for n-array addition. It decomposes it. Every multi-array operation is decomposed into pairs. 

    **eg**

        np.add(a, b, c, d)

        # NumPy breaks this into:
        temp1 = add(a, b)    # C function call 1
        temp2 = add(temp1, c) # C function call 2
        result = add(temp2, d) # C function call 3
    In scala as well complex spark query like 3 joins and filters, the spark catalyst optimizer decomposes into primitive types and executes step by step

- NumPy silently looses its speed in one case, when complete unknown type is passed like object. Then its goes to python basics, runs with python speed.

*Correcting my wring assumption*:
Scala RDD is distributed computation accross the cluster where as NumPy is fast math on a single machine's RAM. They solve completely different problems. Your Spark pipelines process data before it reaches NumPy. NumPy operates on the already-extracted feature matrices inside ML training.
They're not competitors. They're sequential stages.

`My Scala/Spark pipeline processes 2TB of retail pricing data → writes Parquet files → NumPy reads a 4GB feature matrix → ML model trains.`


