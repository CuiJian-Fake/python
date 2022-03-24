x='{0},{0},{0}'.format('dog')
print(x)

format_dic={
    'ymd':'{0.year}{0.month}{0.day}',
    'myd':'{0.month}{0.year}{0.day}',
    'y-m-d':'{0.year}-{0.month}-{0.day}',
}
class Date:

    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def __format__(self, format_spec):
        print('我执行了%s',format_spec)
        if not format_spec or format_spec not in format_dic:
            return '{0.year},{0.month},{0.day}'.format(self)
        else:
            return format_dic[format_spec].format(self)
d1=Date(2016,1,10)
#x='{0.year}{0.month}{0.day}'.format(d1)
# format(d1)
# print(format(d1))
print(format(d1,'aaa'))
