import random

# ret=random.random()
# ret=random.randint(1,3)#1,2,3
# ret=random.randrange(1,3)#1,2
# ret=random.choice([11,22,33])
# ret=random.sample([11,22,33],2)
# ret=random.uniform(11,14)
# print(ret)
# l=[1,2,3,4,5]
# random.shuffle(l)
# print(l)

#验证码
def v_code():

    res=''
    for i in range(4):
        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        alt=chr(random.randint(97,122))
        v=str(random.choice([num,alf,alt]))
        res+=v
    return res

if __name__ == '__main__':
    print(v_code())
