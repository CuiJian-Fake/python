
# #狗的特征
# dog1={
#     'name':'SB',
#     'sex':'母',
#     'type':'藏獒',
#     '属性':'dog'
# }
#
# #狗的动作
#
# def jiao(dog ):
#     print('一条狗[%s]汪汪汪' % dog['name'])
#
# def chi_shi(dog):
#     print('一条狗[%s]正在吃屎' % dog['type'])
#
# jiao(dog1)
# chi_shi(dog1)



def school(name,addr,type ):

    def kao_shi(school):
        print('%s 学校正在考试' %school['name'])

    def zhao_sheng(school):
        print('%s %s 正在招生' % (school['addr'],school['type']))
    def init(name,addr,type):
        school1={
            'name':name,
            'addr':addr,
            'type':type,
            'kaoshi':kao_shi,
            'zhaosheng':zhao_sheng

        }
        return school1
    return init(name,addr,type)
s1=school('oldboy','shahe','sili')
print(s1)
print(s1['kaoshi'](s1))


