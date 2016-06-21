import coverage
cov = coverage.Coverage()
cov.start()

from hello import hello, multiply, MyClass
from notcython import *

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

def test_outside_inside():
    c = MyClass()
    c.outside()

test_outside_inside()

cov.stop()
cov.save()

cov.html_report()
