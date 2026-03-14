colours = ['black', 'white']
sizes = ['s', 'm', 'l']

for t_shirts in ((color, size) for color in colours for size in sizes):
    print(t_shirts)

for t_shirts in ('%s %s' % (color, size) for color in colours for size in sizes):
    print(t_shirts)