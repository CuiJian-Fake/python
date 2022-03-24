class Foo:
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n == 13:
            raise StopIteration('终止了')
        else:
            return self.n

# l=list('hello')
f1=Foo(10)
for i in f1:#iter(f1)------------>f1.__iter__()
    print(i)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())