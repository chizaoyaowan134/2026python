class Computer:
    def __init__(self):
        self.cpu = "i7 处理器"
        self.memory = "16GB 内存"
        print("--- 父类：基础硬件安装完毕 ---")


class GamingLaptop(Computer):
    def __init__(self):
        # 如果不写 super().__init__()，下面这行就会报错
        # 因为这台机器还没装 CPU 和内存呢！
        super().__init__()

        self.gpu = "RTX 4090 显卡"
        print("--- 子类：电竞显卡安装完毕 ---")


# 实例化
my_laptop = GamingLaptop()

print(f"配置清单：{my_laptop.cpu}, {my_laptop.memory}, {my_laptop.gpu}")