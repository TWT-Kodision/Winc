class Person():
    # Class attributes
    home_planet = 'earth'
    species = 'humanity'

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Create new instance
alice = Person('Alice', 20)

# Access class and instance attributes
print(alice.home_planet)
print(alice.age)

def test_example_0():
    assert 1 == 1

def test_example_1():
    assert 1 == 2