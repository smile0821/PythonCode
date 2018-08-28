#coding=utf-8
def print_memu():
    print("============")
    print("------------")

print_memu()

def get_temperature():
    temperature = 28
    print("当前的室温是：%d"%temperature)
    return  temperature
def get_huashi_temp(temp):
    print("当前华氏温度为：%d"%(temp+3))
get_huashi_temp(get_temperature())

#返回多条
def more_return():
    a = 11
    b = 22
    c = 33
    #第1种方式，用列表来封装3个变量的值
    # d = [a,b,c]
    # return d
    #第2种方式，用元组方式
    return a,b,c

print(more_return())