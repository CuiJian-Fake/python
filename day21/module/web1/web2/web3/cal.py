
print('ok1')
def add(*args,**kwargs):
    print(args)
    res=0
    for item in args:
        res+=item
    return res

def sub(a,b):
    return a-b

print('ok2')
print(__name__)
if __name__=='__main__':
    print(add(1,2,3))
