# import json
#
# with open("Josn_test.txt",'r') as f:
#     data=f.read()
#     data=json.loads(data)
#     print(data["name"])

import pickle

dic = {'name':'alvin','age':23,'sex':'male'}
print(type(dic))
j = pickle.dumps(dic)
print(type(j))

f=open('系列化对象_pickle','wb')
f.write(j)
f.close