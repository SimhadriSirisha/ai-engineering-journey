## What it actually is:
Python is an interprested, OOP, high-level programming language with dynamic symantics
Its high-level built-in datastructures combined with dynamic typing and dynamic binding make it very attractive for rapid development
Its a scripting language 
It works in all major platforms like windows, macOS & linux without major changes. 

## Why it was actually created:
It is been created by Guido van rossum as a fun project. Goal is to make the programming language more readable beginner friendly.
It was designed to improve the ABC programming language which lacks exception handling, inability to easily interface with the outside world.

## How it fails silently:
Python uses some reference counter for memory management i.e. for each object whenever its create or referenced, the counter get increment and when the counter becomes 0, we free the object. So when the bytecode run by 2 threads simultaneously, both the threads can try to change the reference counter at the same time and there can be chances of race condition. To avoid this GIL (Global Interpreter lock) is introduced. It feels silent because OS shows 100% CPU usage because CPU tries to do context switching constantly between 2 threads which makes the processing slower and can feel like process got hanged.

This is the one of the biggest reasons why python strugles in high performance distributed system. There is a much bigger picture why scala wins in the world of distributed systems because of its concurrency model. 


## How does Spark work around it?
Python to avoid GIL issue they come up with multiprocessing, where multiple process will be created where each process will have its own memory, to share data between process require serialization which is slow where as scala uses JVM multithreading which utilizes OS native threads which are lightweight, share same memory can spin thousands of thread and share data among them with contant overhead of serializing/deserializing of data.

Python uses mutable objects which is the biggest enemy of distributed systems where as scala uses immutable objects

### How python becomes the favorable programming language for AI/ML world ?
- AI/ML works mostly with complex mathematical equations, which can be executed faster by c/c++ laguage. These AI/ML libraries like NumPy, PyTorch and tensorFlow mostly written in C, C++. Here, python will act as an interface between our code and these libraries. Python pass the pointer(memory optimzation) to our code to C routine making the processing faster. So here we got faster execution and readability at the same time. We are not running the python code when we train a model, we are orchestrating highly optimized binary operations.
- Python’s support for rapid prototyping, it has become the preferred language for researchers. Since the primary goal of AI research is to prove a concept and share results, researchers need a language that feels like writing mathematical pseudocode. Python allows them to implement these ideas quickly, without the extensive boilerplate code required by languages like C++ or Java. Furthermore, its dynamic typing allows for flexibility; you can change a data type on the fly without needing to refactor the entire codebase or go through a lengthy recompilation cycle.

## What surprised me most:
- python acting as a orchestrator

## Source used:
used Gemini to get all the above context