# 普通方法计算阶乘
def recursive(n):
    s = 1
    i = 1
    while i <= n:
        s = s * i
        i = i + 1
    return s


# 阶乘的递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(recursive(30))
print(fact(6))
