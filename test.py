"""a = [1,2,3,4]

def f(x):
    print(x)
    return x+1

print([f(x) for x in a])

g = (f(x) for x in a)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""

"""
a = [1,2,3,4,5]

def g(sec):
    for v in sec:
        if v % 2:
            yield v
        else:
            yield v // 2
            yield v // 2

g1 = g(a)
print(list(g(a)))"""


"""
def g(a):
    for v in a:
        print(v)
        yield v

for v in g(range(10)):
    print(v)
"""

def g(seq):
    for v in seq:
        v1 = yield(v)
        print(v1)


g1 = g([1,2,3,4])
print(next(g1))
print(g1.send("One"))
print(g1.send("Two"))
