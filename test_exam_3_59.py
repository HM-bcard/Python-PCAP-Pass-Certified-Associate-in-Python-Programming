    class A:
        def __init__(self, x=0):
            self.x = x
     
        def func(self):
            self.x += 1
     
     
    class B(A):
        def __init__(self, y=0):
            A.__init__(self, 3)
            self.y = y
     
        def func(self):
            self.y += 1
     
     
    b = B()
    b.func()
    print(b.x, b.y)
