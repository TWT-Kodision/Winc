''''
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

'''
def initials(name):
    first, last = name.split(' ')
    print(first)
    print(last)
    f, l = first[0], last[0]
    return f'{f}. {l}.'

def test_initials_common_name():
    print ("test complete")
    assert initials('Daniel Radcliffe') == 'D. R.'

def test_intials_double_barrelled():
    assert initials('Helena Bonham Carter') == 'H. B. C.'

test_initials_common_name()
test_intials_double_barrelled()
