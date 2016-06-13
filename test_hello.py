from hello import *

def test_hello():
    hello()

def test_multiply():
    c = multiply(5, 6)
    assert(c == 30)

def test_class():
    c = MyClass()
    assert(c.value == 43)
    c.value = 999
    assert(c.value == 999)
