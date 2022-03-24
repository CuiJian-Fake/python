import hashlib #摘要算法

# m=hashlib.md5('sb'.encode('utf-8'))
m=hashlib.md5()
# m.update('admin'.encode('utf-8'))
#
# print(m.hexdigest())
# m.update('root'.encode('utf-8'))
# print(m.hexdigest())
m.update('adminroot'.encode('utf-8'))
print(m.hexdigest())
#4b3626865dc6d5cfe1c60b855e68634a