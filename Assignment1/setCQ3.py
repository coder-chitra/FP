count = 0

def outer(a):
    global count
    count += a

    def inner(b):
        global count
        count += b
        return count

    return inner

f = outer(5)
print(f(10))