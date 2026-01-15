import sys


# print(sys.path)


# 列表推导式：立即占用内存
my_list = [x * x for x in range(10)]

# 生成器表达式：不占用内存，只返回一个生成器对象
my_gen = (x * x for x in range(10))

print(my_gen) # 输出: <generator object ...>

# my_gen = (x * x for x in range(10))
for val in my_gen:
    print(val, end = " ")