class BrokenDog:
    def __init__(self, name):
        self.name = name

    def __eq__(self, value: object) -> bool:
        return self.name == value.name


d1 = BrokenDog("Rex")
d2 = BrokenDog("Rex")

print(hash(d1)) # ❌ TypeError: unhashable type: 'BrokenDog'