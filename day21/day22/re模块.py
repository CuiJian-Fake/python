import re
#元字符 . ^ $ * ? + {} [] | () \
# . 通配符 除了\n 代表任意一个
# * 0到无穷次
# res=re.findall('a..x','adsfaeyxsklg')
# print(res)
# res=re.findall('^a..x','adsxaeyxsklg')
# print(res)
# res=re.findall('s..g$','adsxaeyxsklg')
# print(res)
# res=re.findall('d*s','adsxaeyxsklg')
# print(res)
# res=re.findall('d+s','adsxaeyxsklg')#贪婪匹配 匹配最多
# print(res)
# res=re.findall('d?s','adsxaeydaaasklg')
# print(res)
# res=re.findall('alex?','adsxaeydaaaalexxxxx')
# print(res)
# res=re.findall('alex{0,6}?','adsxaeydaaaalexxxxxx')#家个? 变成惰性匹配 匹配最少
# print(res)
res=re.findall('\([^()]*\)','12+((34*6)+2-5*(2-1))')
print(res)
res=re.search('\([^()]*\)','12+((34*6)+2-5*(2-1))')
print(res.group())
res=re.findall('\d+','12+(34*6+2-5*(2-1))')
print(res)
# res=re.findall('\D+','12+(34*6+2-5*(2-1))')
# print(res)
# res=re.findall('\s','hello world')
# print(res)
# res=re.findall('\S','hello world')
# print(res)
# res=re.findall('\w+','123 hello world')
# print(res)
# res=re.findall('I\\b','I am LIST')
# print(res)
# res=re.findall(r'I\b','I am LIST')#python解释器要穿给re模块\b 解释器需要正常传入 不转义\b
# print(res)
# res=re.findall(r'c\\l','abc\lerwt')
# print(res)
# res=re.findall(r'ka|b','awedawedka|bedawedakb')
# print(res)
# # res=re.findall('(abc)+','abcabcabc')
# # print(res)
# res=re.findall('(?P<name>\w+)','awedawedka|bedawedakb')
# print(res)
# res=re.search('(?P<name>\w+)','awedawedka|bedawedakb')#返回第一个 对象形式
# print(res)
# print(res.group())
# res=re.search('(?P<name>[a-z]+)(?P<age>\d+)','aaa36wusir22xialn21')#分组提取
# print(res.group('age'))
# res=re.match('\d+','hfdkuahfki12')#从开头匹配
# print(res.group())
# res=re.match('\d+','233hfdkuahfki12')
# print(res.group())
# res=re.split(' ','hello alex csgo')
# print(res)
# res=re.split('[ |]','hello alex|csgo')
# print(res)
# res=re.findall(r'ka|b','awedawedkaabedawedkakb')
# print(res)
# res=re.split('[ab]','asdabcd')
# print(res)
res=re.sub('\d+','A','ajdfhli2ihu2h3khkh213',2)
print(res)
res=re.subn('\d+','A','ajdfhli2ihu2h3khkh213')
print(res)
# com=re.compile('\d+')
# res=com.findall('123asdfadfadf')
# print(res)
# res = re.finditer('\d+', 'ajdfhli2ihu2h3khkh213')
# print(res.__next__().group())
# print(res.__next__().group())
# print(res.__next__().group())
# print(res.__next__().group())
# # print(res.__next__().group())
# res = re.findall('www\.(?:baidu|163)\.com', 'aedawedwww.baidu.com')  # 优先默认返回baidu 可以加？：去掉优先级可以直接拿到字符串
# print(res)
res=re.findall('(?:abc)+','abcabcabcddabc')
print(res)
