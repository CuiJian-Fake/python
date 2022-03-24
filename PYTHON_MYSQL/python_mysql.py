'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 4/2/2021 10:32 AM
@Software: PyCharm
@File    : python_mysql.py
'''
import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='Cj')

cursor = conn.cursor()

sql="CREATE TABLE T2(id INT,name VARCHAR(20))"

cursor.execute(sql)

cursor.execute("INSERT INTO T2 values(1,'alex'),(2,'yuan')")
RET=cursor.execute("select * from T2") #返回结果是行数 2
print(RET)
print(cursor.fetchone())
print(cursor.fetchmany(2))
print(cursor.fetchall())

conn.commit()
cursor.close()
conn.close()
cursor.scroll(1,mode="relative")#整数 负数反向 相对位置
cursor.scroll(1,mode="absolute")#绝对位置 游标

#ORM操作数据库 代替sql语句 操作数据库

def check():

a=rdpcap('/root/HB.pcap')
a.show()
for i in range(0,1148):
    p=a[i]
    sendp(p,iface='ens785f1')







