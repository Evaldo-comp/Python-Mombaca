a=[1,2,3,4,6,7]
def f(l):
    b = ""
    for x in a:
        b += str(x)
    return int(b)

print(f(a))