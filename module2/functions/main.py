# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
from turtle import end_fill


def greet(name):
    say_hello = "Hello, " + name +"!"
    return say_hello

print(greet("Name"))

def add(a,b,c):
    sum=a+b+c
    return sum

print (add(1.3369,2,3))

def positive(number):
    is_positive = number>0
    return is_positive
print(positive(0))

def negative(number):
    is_negative = number<0
    return is_negative
print(negative(0))
