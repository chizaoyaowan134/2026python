def function_c():
    print("开始执行 C")
    result = 10 / 0  # 这里会发生 ZeroDivisionError
    print("这一行不会执行")

def function_b():
    print("开始执行 B")
    function_c()    # B 调用了 C，但 B 也没有处理异常
    print("B 的后续也不会执行")

def function_a():
    try:
        print("开始执行 A")
        function_b() # A 调用了 B
    except ZeroDivisionError as e:
        # 异常最终在这里被接住了！
        print(f"在 A 中捕获到了来自 C 的异常: {e}")

function_a()