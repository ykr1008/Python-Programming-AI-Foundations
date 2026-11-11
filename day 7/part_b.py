class Dog:
tricks = []
def __init__(self, name): self.name = name
a = Dog('Rex'); b = Dog('Bo')
a.tricks.append('roll')
print(b.tricks)

# Predicted and verified: it prints ['roll']. tricks is a class attribute, so every Dog shares 
# the one list, and a.tricks.append(...) mutates that shared list rather than creating anything on a.

# fix
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []