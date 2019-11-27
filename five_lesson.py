class Iterator:
    def __init__(self, container):
        self.container = container
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.container.n:
            raise StopIteration()
        self.i += 1
        return self.i - 1

class MyRange:
    def __init__(self, n):
            self.n = n
    def __iter__(self):
        return Iterator(self)

r = MyRange(5)
for i in r:
    print(i)