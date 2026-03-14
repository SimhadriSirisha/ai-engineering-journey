colours = ['black', 'white']
sizes = ['s', 'm', 'l']

# list comprehension
t_shirts = [(colour, size) for colour in colours for size in sizes]
print(t_shirts)

t_shirts2 = [(color, size)
             for size in sizes
             for color in colours]
print(t_shirts2)

# normal for loop 
for color in colours:
    for size in sizes:
        print((color, size))