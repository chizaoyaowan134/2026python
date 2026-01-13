class Phone:
    # 1. 类属性：所有手机共享的信息
    total_count = 0  # 累计生产总数
    factory_name = "全宇宙智能制造工厂"

    def __init__(self, model):
        # 2. 实例属性：每台手机自己的型号
        self.model = model

        # 重点：每生产一台手机（执行一次__init__），类属性就加 1
        Phone.total_count += 1
        print(f"成功生产一台 {self.model}")

    # 3. 类方法：专门用来处理类属性
    @classmethod
    def show_factory_report(cls):
        # cls 代表类本身，相当于 Phone
        print(f"--- 工厂报告 ---")
        print(f"所属工厂：{cls.factory_name}")
        print(f"当前生产线累计产量：{cls.total_count}")


# --- 开始操作 ---

# 生产 3 台不同的手机
p1 = Phone("iPhone 15")
p2 = Phone("Mate 60")
p3 = Phone("Xiaomi 14")

# 调用类方法查看汇总信息
Phone.show_factory_report()