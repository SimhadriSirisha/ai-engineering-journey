## How classes created ?
small class which i have seen in the file
```
class ParamTypes(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"
```

## What is Pydantic ?
Pydantic is a data validation library. 
It's one job is : `Take outside data, validate and convert it into python types`.

### **3 Things it does** :
- Validation

    **eg**:
    ```
        product = Product(name="Phone", price=999.0)   # ✓ works
        product = Product(name="Phone", price=-5)      # ✗ ValidationError — price must be > 0
        product = Product(price=999.0)                 # ✗ ValidationError — name is required
    ```
- Type Coercion : converts 1 type to another silently, if not possible raises error.

    **eg**:
    ```
        # price comes in as a string from JSON — very common
        product = Product(name="Phone", price="999")
        # Pydantic converts "999" → 999.0 automatically
        # product.price is now float, not string
    ```
- Serialization : converts objects back to dict/JSON

    **eg**:
    ```
    product = Product(name="Phone", price=999.0)

    product.model_dump()
    # → {"name": "Phone", "price": 999.0}   ← Python dict

    product.model_dump_json()
    # → '{"name": "Phone", "price": 999.0}'  ← JSON string

    Convert your validated object back to dict or JSON for storing or sending.
    ```
### **Why FastAPI uses it:**
- HTTP requests arrive as raw strings.
- Pydantic converts and validates before your code runs.
- Bad data never reaches business logic.

### **Why critical for AI engineering:**
- Validates LLM structured outputs (did LLM return correct schema?)
- Validates API inputs before reaching ML model
- Validates configs at startup before pipeline runs

### **Silent failure without it:**
- Wrong types reach ML model → unpredictable behaviour.
- LLM returns wrong structure → crash deep in pipeline.
- Bad config → 3am production failure.

## What is this syntax - `annotation: Any | None = None` :
- These are type hints with generic syntax as `param: TypeA | None = default_value`
- This says param is of either typeA (int, str, ..etc) or can be None, if nothing given then takes the default value.
- **Why its created** : It created as an information to the devs without reading the whole code and understand about the type of param
    
    **eg**:
    `def create_field(annotation, alias, alias_priority):` - this doesn't say clearly what is the type of the parameters, can I pass None. Is the parameter needed, mandatory
- **Where it fails silently** : 
    **eg**
    ```
    def create_field(alias: str | None = None):
        return alias.upper()

    create_field(alias=123)
    ```
    This will not fail, this code will fail at runtime when called as alias.upper() with attribute error and not as type error.
    So that means TypeHints are just documentation. These are hints for tools (mypy) and libraries (Pydantic).
-  **_Unset pattern** : used when you need to distinguish between
    "not provided" vs "explicitly set to None" — two different
    cases that = None alone cannot separate.
- **FastAPI usage**: FastAPI specifically uses **Pydantic under the hood** which DOES enforce types at the boundary — when a request comes in. That's why FastAPI can say "you sent an int, I expected a string" and return a proper error to the caller.

### What is `*` in the below def:
```
def __init__(self, default, *, annotation):
    pass
```
`*` is not `*args`, this single `*` is *keyword-word only* seperator. It tells that parameters after `*` should be passed as named parameter only otherwise its throws as TypeError

**eg**

```
Field("hello")                    # default="hello" ✓ positional works
Field("hello", str)               # annotation=str  ✗ FAILS — must use name
Field("hello", annotation=str)    # ✓ correct
```
- **Why its introduced**: If in future, if the parameters were then these named parameters will help otherwise all the callers either take wrong values of type is same otherwise throws `TypeError`.
    - This forces users to be explicit
- **Rule** : 
    - before *  →  can be positional or named
    - after  *  →  MUST be named, no choice

#### `Undefined` as default value:
This is a sentinel value. This is a unique object. Its purpose it to tell that user has not provided.
This differentiate between `None` and `Not Provided`. 
- **Why to differentiate?** : Because `None` is a valid bussiness value.
- Check with `is` not `==` — identity check, not equality.
- **Three states it enables:**
    - value is Undefined  → caller never passed anything → field is REQUIRED
    - value is None       → caller explicitly passed None → field is optional
    - value is something  → use that value
- **What `Undefined` as default Actually Means**: It means: "the caller did not provide a value, so Pydantic will apply its own internal logic to decide what to do next."
    it doesn't mean the parameter is compulsory. It cumpolsury is decided by Pydantic library through varius checks. i.e.:
    - Pydantic then applies its own logic:
        - no default + no factory → field is REQUIRED in the model
        - no default + factory exists → call factory to generate default
        - real default given → field is optional
    
    **eg**:
    ```
    # Case 1 — Undefined + nothing else → REQUIRED
    Field(default=Undefined)

    # Case 2 — Undefined + factory given → use factory
    Field(default=Undefined, default_factory=list)
    
    # Case 3 — real value → optional
    Field(default=0.0)
    ```

### Explain this pattern `Annotated[actual_type, metadata1, metadata2, ...]`:
- This gives extra information to the parameter/variable without changing the type.
- **Actual use**: The metadata written is a m/c readable, this will be understandable by the libraries like Pydantic otherwise missed be library and user. 

    **eg**
    ```
    regex: Annotated[str | None, deprecated("Deprecated in FastAPI 0.100.0...")] = None
    ```
    this tells the library that regex is deprecated, and the FastAPI can strike through when we use regex.
    If used as comment mostly missed by users and if used in production code, then there can be a silent failures.

### Pattern: **extra: Any
Collects all unrecognised keyword arguments into a dict.
Used by framework authors for forward compatibility.
DANGEROUS in application code — swallows typos silently.
Rule: acceptable in library internals, avoid in your own application code.
Silent failure: typo in parameter name → goes into **extra → 
wrong behaviour, zero error.

### A variable name with trailing underscore (variable_) 
If the variable is a reserved word, then to use it as a variable we add a trailing `_`.

### Pattern: ... (Ellipsis) as default value. `param: Any = ...`
This tell Pydantic that parameter is compulsory there is no default value for it.
`...` is a real Python built-in object (ellipsis type).
Pydantic v1 convention: default=... means field is REQUIRED.
Different from None (explicit optional) and Undefined (v2 sentinel).

## What is a TypeVar ? Syntax: `TypeVar('T', dataType1, dataType2, ...)`
- TypeVar is a static type checker, where its not for python, it is for static type checker tools like myph. Gives hints to static tools only.
- **Difference between static & dynamic**:
    - Static  = before runtime, while reading/analysing code
    - Dynamic = during runtime, while code is actually executing
- Python is Dynamic type checker. Type checks happen at runtime that too if any method doesn't work that varible the Attribute error comes but not Type error. But due to Pydantic, getting ri8 errors
- TypeVar does not make Python static. It gives static tools **enough information to trace types across function boundaries.**
- **How TypeVar helps static checkers**: TypeVar give information to static type checker, and those checker read the code and understand it, if in the code if anywhere type challenged then it can find before running.
```
T = TypeVar("T")

def identity(x: T) -> T:
    return x

def process(data):
    result = identity(data)
    result.upper()

result = identity("hello")

mypy reads this **without running it**:
1. identity is called with "hello"
2. "hello" is a str
3. T is bound to str for this call
4. return type is T, which is str
5. therefore result is str
```
- **Why at runTime not possible to catch**: RunTime error can be catched if the function `identity(x: T)` called with wrong type other than `str` because process def fails at `result.upper()` then only it will find otherwise can't
- **TypeVar vs Type hints**:
    - Type hint  = documents what ONE thing should be
    - TypeVar    = documents RELATIONSHIP between types across a function
            "whatever type comes in, same type comes out"
- **Why does isinstance(x, T) raise TypeError?** TypeVar is not a real class at runtime.
It is a placeholder for static analysis only.
isinstance needs a real class. T is not one.
Rule: TypeVar is meaningless at runtime for checks.
```
isinstance(x, int)    # ✓ works — int is a real class
isinstance(x, str)    # ✓ works — str is a real class
isinstance(x, T)      # ✗ TypeError — T is not a real class

TypeVar lives in two worlds:
  Static analysis world  → meaningful, expresses relationships
  Runtime world          → just an object, cannot be used for checks
```
- **What is TypeVar with bound ?** It bounds or strongly tells that its bound be of that type only. eg: `DecoratedCallable = TypeVar("DecoratedCallable", bound=Callable[..., Any])`
- TypeVar returns an object, as TypeVar is a class & python allows to have object as return type

## What is Callable ?
Callable is a type hint, which tells that the parameter type callable should be function only.
- In python, functions are objects, can be passed as parameter to a function, store them in a variable and return from another function as well
```
def greet(name: str) -> str:
    return f"Hello {name}"

# greet is a Callable object
print(type(greet))   # <class 'function'>
```
- Syntax : Callable[[input_types], return_type]
```
Callable[[str], int]        # takes str, returns int
Callable[[int, float], str] # takes int and float, returns str
Callable[..., Any]          # takes anything, returns anything | ... means "I don't care about the input parameters — any signature is fine."
```

## Decorator 
Foundation:
A function in python is a object, can be stored, can be returned and can be passed as a parameter.

Eg of `function returning a function`:
```
def make_multiplier(n):
    
    def multiply(x):       # function defined INSIDE another function
        return x * n
    
    return multiply        # returning the function itself, not calling it

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # → 10
triple(5)   # → 15
```

A Decorator is a function which takes a function and returns a function
```
def logger(func):              # takes a function as input
    
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)     # calls the original function
        print(f"done")
        return result
    
    return wrapper             # returns a NEW function


def add(a, b):
    return a + b

# manually wrapping
add = logger(add)

# now add points to wrapper, not the original add
add(2, 3)
# prints: calling add
# prints: done
# returns: 5
```

#### The @ Syntax
This is a pure syntax sugar, it doesn't has any new meaning just makes the representation good. It is the replacement of method call with a function.
```
# These two are identical:

# Without @
def add(a, b):
    return a + b
add = logger(add)


# With @
@logger
def add(a, b):
    return a + b
```
By seeing `@`, python will call the method logger with add and reassign the name with return method of logger

#### What `*args` and `**kwargs` Are Doing in Wrapper ?
```
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```
The wrapper doesn't know what arguments the original function takes.
- *args : takes all positional arguments
- **kwargs : takes all keyword arguments into a dict
```
@logger
def add(a, b):
    return a + b

add(2, 3)
# wrapper receives args=(2, 3), kwargs={}
# calls func(2, 3) → original add(2, 3)
# returns 5
```

#### Decorator With Arguments
```
@app.get("/users")
def get_users():
    ...
```
This `@app.get("/users")` means get() is first called with parameter `"/users"` and returns the decorator and then that decorator called with get_users and python re-assigns the returned method to the name
```
# This:
@app.get("/users")
def get_users():
    ...

# Is exactly this:
decorator = app.get("/users")   # call get() with "/users", get a decorator back
get_users = decorator(get_users)  # apply that decorator to the function
```

#### With and Without TypeVar
DecoratedCallable TypeVar = ensures decorator preserves the exact type of the function it wraps.
Without it: type information lost, autocomplete breaks downstream.
```
# WITHOUT TypeVar
@app.get("/price")
def get_price() -> float:
    return 99.0

result = get_price()
result + 1        # ✗ mypy error — thinks result is Any, not float


# WITH TypeVar
@app.get("/price")
def get_price() -> float:
    return 99.0

result = get_price()
result + 1        # ✓ mypy knows result is float


## The Mental Model in One Line
Without TypeVar:  decorator is a BLACK BOX — type goes in, unknown comes out
With TypeVar:     decorator is a TRANSPARENT BOX — type goes in, same type comes out
```