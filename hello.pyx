def hello():
    print("Hello, World!")

cpdef multiply(a, b):
    return a * b

cdef class MyClass:
    cdef int n

    def __cinit__(self):
        self.n = 42

    def __init__(self):
        self.n += 1
    
    property value:
        def __get__(self):
            return self.n
        def __set__(self, value):
            self.n = value

meh = MyClass()
meh.value = 88
            
foo = "bar"
