class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)
    def __del__(self):
        print("%s 我去了" % self.name)
    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name

# tom = Cat("Tom")
# print(tom)

# 请你分析下面代码的执行结果，并解释原因
cat1 = Cat("大毛")
cat2 = cat1
cat3 = cat2
print(id(cat1))
print(id(cat2))
print(id(cat3))

# 代码执行结果：
# 大毛 来了
# 140703614123184
# 140703614123184
# 140703614123184
# 大毛 我去了
# 解释原因：
# 1. 创建 cat1 对象时，调用 __init__ 方法，打印 "
# 大毛 来了"。
# 2. cat2 和 cat3 都是对 cat1 的引用，因此它们
# 的 id 与 cat1 相同。
# 3. 删除 cat1、cat2 和 cat3 后，引用计数变
# 为 0，调用 __del__ 方法，打印 "大毛 我去了"。


