def check_age(age):
    # 检查传入的年龄是否在合理范围内（0 到 150）
    if age < 0 or age > 150:
        # 主动抛出异常，并给出错误说明，调用方可以捕获这个 ValueError
        raise ValueError("年龄不合法：必须在 0 到 150 岁之间")
    # 年龄合法时输出登记成功的信息
    print(f"年龄登记成功：{age}")

try:
    # 测试用例：传入非法年龄会触发异常
    check_age(-10)
except ValueError as e:
    # 捕获到 ValueError 后将异常信息打印出来，便于调试或提示用户
    print(f"捕获到了错误：{e}")