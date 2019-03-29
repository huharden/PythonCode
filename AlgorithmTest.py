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


print(my_abs(-44))
print(multiple(2, 4))
