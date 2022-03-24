import time

# print(time.time())#从1970年凌晨到现在经历了多少秒 时间戳
# print(time.localtime())
# t=time.localtime()
# print(time.gmtime())
# print(t.tm_year,t.tm_wday)
# print(t.tm_isdst)
#
# #将结构化时间转换成时间戳
# print(time.mktime(time.localtime()))
#将结构化时间转换成字符串时间
# print(time.strftime("%Y-%m-%d %X",time.localtime()))
# print(time.strptime("2019:12:20:17:50:36","%Y:%m:%d:%X"))
# print(time.asctime())
# print(time.ctime())

import datetime

print(datetime.datetime.now())