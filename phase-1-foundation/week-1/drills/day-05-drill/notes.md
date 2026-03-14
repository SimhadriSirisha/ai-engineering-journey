- when we print this string: "C:\new\file", its output will be:
```
    C:
    ew
        ile
``` 
because here backslash are escape characters, here \n & \f are interpreted as escape sequences. But if we prefix string with r"C:\new\file", then its output is `C:\new\file`

- In Python source, a backslash at the end of a physical line means “continue this logical line on the next line”.
```
string = "It was the best of times,\n\
It was the worst of times."
```
So above 2 lines are treated as single line:
```
'It was the best of times,\nIt was the worst of times.'
```

- Adjacent string are concated automatically 
```
string = "Hello" ", " "world" # string = Hello, world
```

- 