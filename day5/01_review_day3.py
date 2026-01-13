# # 1. 定义外层循环变量，控制行
# row = 1
#
# while row <= 9:
#     # 2. 定义内层循环变量，控制列
#     col = 1
#
#     while col <= row:
#         # 3. 打印乘法公式
#         # end="\t" 的作用是打印后不换行，而是增加一个制表符，使对齐更整齐
#         print(f"{col} * {row} = {col * row}", end="\t")
#
#         # 内层循环变量自增
#         col += 1
#
#     # 4. 当一列打印完毕后，打印一个换行符，开始下一行
#     print("")
#
#     # 外层循环变量自增
#     row += 1


# def test(num):
#     print("-" * 50)
#     print("%d 在函数内的内存地址是 %x" % (num, id(num)))
#     result = 100
#     print("返回值 %d 在内存中的地址是 %x" % (result, id(result)))
#     print("-" * 50)
#     return result
#
# a = 10
# print("调用函数前 内存地址是 %x" % id(a))
# r = test(a)
# print("调用函数后 实参内存地址是 %x" % id(a))
# print("调用函数后 返回值内存地址是 %x" % id(r))



# a = [x for x in range(10)]
# print(a)
# b = []
# for x in range(10):
#     b.append(x)
# print(b)
# # 2 个 for 循环
# a = [j for i in range(10) for j in range(i)]
# print(a)
# a = [[col * row for col in range(5)] for row in range(5)]
# print(a)
# a = [j for x in a for j in x]  # 2 维列表转 1 维列表
# print(a)
# # 只有 if 时
# a = [x for x in range(10) if x % 2 == 0]  # 将只会筛选偶数
# print(a)
# # if-else 的三元表达式
# a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
# print(a)


# 请你给出截取字符串末尾两个字符

s = "abcdefgh"
# result = s[-2:]
# print(result)

# 他的原理是什么？
# 负索引表示从字符串的末尾开始计数，-1 是最后
# 一个字符，-2 是倒数第二个字符。
# 切片操作 s[-2:] 表示从倒数第二个字符开始，一
# 直到字符串的末尾，提取出这部分子字符串。
# 因此，result 的值就是 "gh"。

# 字符串的逆序
# reversed_s = s[::-1]
# print(reversed_s)
# 他的原理是什么？
# 切片操作 s[::-1] 使用了步长为 -1，这表示从
# 字符串的末尾开始，向前遍历整个字符串，逐个取
# 字符，最终形成一个新的字符串，即原字符串的逆序。
# 因此，reversed_s 的值就是 "hgfedcba"。


# issuperset()的例子

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3}
# result = set1.issuperset(set2)
# print(result)  # 输出: True

'''
# 他的原理是什么？
issuperset() 方法用于判断一个集合是否是另一个集合的超集。
在这个例子中，set1 包含元素 {1, 2, 3
, 4, 5}，而 set2 包含元素 {2, 3}。
由于 set1 包含了 set2 的所有元素（2 和 3），
因此 set1 是 set2 的超集，issuperset() 方法返回 True。
'''
#
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# t_list = [1, 1]
# print(t_list)



t1 = (1, 2)
t2 = (1, 2)
print(t1 is t2)
print(id(t1))
print(id(t2))