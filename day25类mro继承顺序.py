class A:
    def test(self):
        print('A')
class B(A):
    # def test(self):
    #     print('B')
    pass

S1=B()

S1.test()