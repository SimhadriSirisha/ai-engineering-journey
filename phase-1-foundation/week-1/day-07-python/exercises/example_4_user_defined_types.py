class Dog:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, object) -> bool:
        return self.name == object.name # now compares data, not address

    def __hash__(self) -> int:
        return hash(self.name) # now hashes data, not address

d1 = Dog("Rex")
d2 = Dog("Rex")

print(d1 == d2)        # ✅ True — same name
print(hash(d1) == hash(d2))  # ✅ True — same hash