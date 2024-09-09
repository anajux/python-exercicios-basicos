
a = 1
b=2
def f():
    a=2
    c=3
    def g(*args):
        d = args[0] + args[1]
        print(d)
    b = 5
    g(a,b,c)
f()