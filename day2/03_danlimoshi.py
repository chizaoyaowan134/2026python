class MusicPlayer:
    # 定义一个类属性，记录第一个被创建对象的引用
    _instance = None

    # 定义一个标志，记录初始化动作是否执行过
    _init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls._instance is None:
            # 2. 调用父类的方法，为第一个对象分配内存
            cls._instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls._instance

    def __init__(self):
        # 如果不加这个判断，每次调用 MusicPlayer() 都会重新初始化属性
        if not MusicPlayer._init_flag:
            print("初始化播放器，加载音乐库...")
            MusicPlayer._init_flag = True


# --- 测试单例效果 ---
player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1 is player2)  # 输出: True
print(id(player1))  # 地址完全一样
print(id(player2))  # 地址完全一样