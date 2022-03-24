# from cal import add,sub
from module.web1.web2.web3 import cal
from module.web1.web2 import web3 #执行web3的init文件，记住都是别用
#if __name__=='__main__': 不要让别人调用你的文件 自测
# print(cal.add(2,3,4))
# print(cal.sub(2,3))
print(web3.cal.add(2,3))
print(__name__)
