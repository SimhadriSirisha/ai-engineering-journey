class CatchAllAttributeReads:
    def __getattribute__(self, attr_name):
        return "Someone called '" + attr_name + "' and it could not be found"

catcher = CatchAllAttributeReads()
print(catcher.foobar)
print(catcher.foobaz)

try:
    catcher.foobaz(1)
except TypeError as ex:
    err_msg = ex.args[0]

print(err_msg)

try:
    "foobaz"(1)
except TypeError as ex:
    err_msg = ex.args[0]

print(err_msg)

string = "It was the best of times,\n\
It was the worst of times."
print(len(string))

s = """
Howdy,
world!
"""
print(len(s))