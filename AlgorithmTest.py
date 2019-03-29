def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 次方函数运算, n=2为默认值
def multiple(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可变参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(my_abs(-44))
print(multiple(2, 4))
print(abs(4))
print(person("小明", "5", city='Beijing', sex='女'))
