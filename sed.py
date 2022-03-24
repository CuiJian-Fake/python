#!/usr/bin/env python
#coding:utf-8
#函数
#文件处理
#tag的用法
#程序的解耦
import os
def handler(backend_data,res=None,type='fetch'):
    if type == 'fetch':
        with open ('haproxy.conf','r') as f:
            tag = False
            res = []
            for read_line in f:
                if read_line.strip() == backend_data:#strip默认去除回车空格可以指定字符
                    tag = True
                    continue
                if tag and read_line.startswith('backend'):
                    break
                if tag:
                    print('\033[1;45m%s\033[0m' %read_line,end='')
                    res.append(read_line)
                # if not tag:
                #     pass
            return res
    else:
        with open('haproxy.conf', 'r') as f_read, open('haproxy.conf_new', 'w') as f_write:
            tag = False
            has_write = False
            for read_line in f_read:
                if read_line.strip() == backend_data:
                    tag = True
                    continue
                # if tag and read_line.startswith('backend'):
                if tag:
                    if not has_write:
                        for record in res:
                            f_write.write(record)
                        has_write = True
                if tag and read_line.startswith('backend'):
                    tag = False
                if not tag:
                    f_write.write(read_line)
        os.rename(
            'haproxy.conf', 'haproxy.conf.bak'
        )
        os.rename(
            'haproxy.conf_new', 'haproxy.conf'
        )
        os.remove('haproxy.conf.bak')

        return res

def fetch(data):
    print('正在查询')
    print('\033[1;43m用户输入的数据:\033[0m%s' %data)
    backend_data='backend %s' %data
    print(backend_data)
    # with open ('haproxy.conf','r') as f:
    #     tag = False
    #     res = []
    #     for read_line in f:
    #         if read_line.strip() == backend_data:#strip默认去除回车空格可以指定字符
    #             tag = True
    #             continue
    #         if tag and read_line.startswith('backend'):
    #             break
    #         if tag:
    #             print('\033[1;45m%s\033[0m' %read_line,end='')
    #             res.append(read_line)
    #         # if not tag:
    #         #     pass
    #     return res
    return handler(backend_data)
def add():
    pass

def change(data):
    print('这是修改功能')
    print('用输入的数据是',data)
    backend=data[0]['backend']
    backend_data='backend %s'%backend
    new_backend_data='backend %s'%data[1]['backend']
    old_server_record='%sserver %s %s weight %s maxconn %s\n' %(' '*8,data[0]['record']['server'],
                                                              data[0]['record']['server'],
                                                              data[0]['record']['weight'],
                                                              data[0]['record']['maxconn'])
    new_server_record='%sserver %s %s weight %s maxconn %s\n' %(' '*8,data[1]['record']['server'],
                                                              data[1]['record']['server'],
                                                              data[1]['record']['weight'],
                                                              data[1]['record']['maxconn'])
    print('用户想要修改的记录',old_server_record)

    res=fetch(backend)
    if not res or old_server_record not in res:
        return '你要修改的记录不存在'
    else:
        index = res.index(old_server_record)
        res[index]=new_server_record#替换需要修改的内容
        res.insert(0,'%s\n'%new_backend_data)
        return (handler(backend_data,res=res,type='change'))


def delete():
    pass

if __name__=='__main__':
    # print(__name__)
    msg='''
    1:查询
    2:添加
    3:修改
    4:删除
    5:退出
    '''
    msg_dic={
        '1':fetch,
        '2':add,
        '3':change,
        '4':delete,
    }
    while True:
        print(msg)
        choose=input('请输入你要操作的指令：').strip()#strip 去空格回车
        if not choose:continue
        if choose == '5':break
        data=input('请输入你的数据：').strip()
        if choose != '1':
            data=eval(data)
        res=msg_dic[choose](data)
        print(res)

[{'backend':'www.oldboy10.org','record':{'server': '10.10.10.1','weight':22,'maxconn':2000}},{'backend':'www.oldboy1000.org','record':{'server': '6.6.6.6','weight':66,'maxconn':6666}}]

