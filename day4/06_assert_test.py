# 区别：
# - 模块顶层的 assert 被放在 try/except 里：断言失败会抛出 AssertionError，
#   但被 except Exception 捕获并处理，因此程序不会中断。
# - 函数内部的 assert（例如在 send_red_packet 内）：断言在函数内部触发，
#   若调用者没有捕获 AssertionError，异常会向上抛出并导致程序中断。
#
# 额外注意：
# - AssertionError 是 Exception 的子类，所以用 except Exception 可以捕获它。
# - assert 主要用于调试；当使用 Python 的 -O（优化）选项运行时，assert 会被忽略，
#   因此不应把 assert 当作关键业务校验手段。
#
# 建议做法：
# - 对函数输入做业务校验时，使用显式判断并抛出合适的异常（例如 ValueError）：
#   # 示例（注释形式）：
#   # def send_red_packet(money):
#   #     if money <= 0:
#   #         raise ValueError("红包金额必须大于 0！")
#   #     print(f"成功发出 {money} 元红包")
#
# - 调用可能抛出异常的函数时，在调用处进行捕获并处理：
#   # 示例（注释形式）：
#   # try:
#   #     send_red_packet(-5)
#   # except ValueError as e:
#   #     print("发送失败：", e)
#
# 总结：
# - 用 assert 做快速调试断言可以方便定位问题，但不要依赖它做生产环境的参数校验；
# - 生产校验应使用 if + raise，并在调用处根据需要捕获并处理特定异常。



# try:
#     assert 1 == 0, "你的程序在这里发生了什么什么错误"
# except Exception as e:
#     print(e)

def send_red_packet(money):
    # 我断言 money 一定大于 0，否则就是程序逻辑出了严重问题
    assert money > 0, "红包金额必须大于 0！"

    print(f"成功发出 {money} 元红包")


# 正常调用
send_red_packet(10)

# 异常调用
send_red_packet(-5)
# 结果：程序直接中断，抛出 AssertionError: 红包金额必须大于 0！