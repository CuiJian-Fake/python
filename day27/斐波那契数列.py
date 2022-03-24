class Fbnq:

    def __init__(self):
        self._a=1
        self._b=1

    def __iter__(self):
        return self

    def __next__(self):
        self._a,self._b=self._b,self._a+self._b
        #                     1           2
        # 1           2
        #                     2           3
        # 2           3
        #                      3           5

        return self._b
f1=Fbnq()
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())