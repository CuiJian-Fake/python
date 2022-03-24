import json

#把数据的单引号都变成双引号,最后在加上一个单引号

dic = {'name':'alex'}
# data=json.dumps(dic)
# print(data)
# print(type(data))

f=open('JJJ.txt','w')
json.dump(dic,f)
f.close()

f_read=open('JJJ.txt','r')
v=json.loads(f_read.read())
print(v)
print(type(v))