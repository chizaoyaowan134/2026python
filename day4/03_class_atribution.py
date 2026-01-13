class Tool:
    count = 10  # 类属性

# 创建对象
t1 = Tool()
t2 = Tool()

# 1. 初始状态：大家都在用类属性
print(t1.count)  # 输出 10
print(Tool.count) # 输出 10

# 2. 关键操作：给 t1 赋值
t1.count = 99

# 3. 查看结果
print(t1.count)    # 输出 99（t1 自己有了 count 属性，不再用类的了）
print(t2.count)    # 输出 10（t2 自己没有，依然去类里借，类还是 10）
print(Tool.count)  # 输出 10（类属性稳如泰山，没被修改）