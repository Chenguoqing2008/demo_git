
def generator():
    for i in range(10):
        b = yield i
        if b is None:
            i += 1
            print(i)


a = generator()
print(a)
print(a.__next__())
# print(a.send(2))
print(a.__next__())
# print(a.__next__())
