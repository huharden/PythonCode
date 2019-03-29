# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L = list(range(100))
# 切片特性[1:4]表示从索引1开始，知道索引4
print(L[1:5])
print(L[-1:])
print(L[:])

# tuple也知道切片操作
T = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(T[-4:-2])


# 利用切片操作去除字符串的首尾空格
def trim(s):
    i = 0
    j = len(s)
    while i < j and s[i] == " ":
        i = i + 1
    while j > 0 and s[j - 1] == " ":
        j = j - 1
    return s[i:j]


str1 = str(input('请输入：'))
print(trim(str1))
