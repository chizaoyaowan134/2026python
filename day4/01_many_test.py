
# def demo(num, *args, **kwargs):
#     print(num)
#     print(args)
#     print(kwargs)
#
#
# demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)


# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     # 需要将一个元组变量/字典变量传递给函数对应的参数
# gl_nums = (1, 2, 3)
# gl_xiaoming = {"name": "小明", "age": 18}
#     # 会把 num_tuple 和 xiaoming 作为元组传递个 args
#     # demo(gl_nums, gl_xiaoming)
#
#
# demo(*gl_nums, **gl_xiaoming)

#如果有 n 个台阶，每次只能走 1 个，或者 2 个台阶，到第 n 个台阶有多少种走法？

def countWays(n):
    """
    计算爬上 n 个台阶有多少种走法。
    这是一个典型的斐波那契数列问题：
    - 到第 n 阶的走法 = 到第 n-1 阶的走法 + 到第 n-2 阶的走法
    
    :param n: 台阶的总数
    :return: 走法的总数
    """
    # 递归的出口：如果台阶数为 1 或 2
    # 1 个台阶只有 1 种走法 (1)
    # 2 个台阶有 2 种走法 (1+1, 2)
    if n <= 2:
        return n
    else:
        # 递归调用：当前台阶的走法等于前一级台阶走法加上前两级台阶走法之和
        return countWays(n - 1) + countWays(n - 2)

num = countWays(10)
print(num)