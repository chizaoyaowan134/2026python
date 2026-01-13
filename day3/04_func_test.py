def test(num):
    """
    测试函数：打印形参和返回值的内存地址
    :param num: 接收外部传入的实参
    :return: 返回一个整数 result
    """
    print("-" * 50)
    # id() 函数用于获取对象的内存地址，%x 表示以十六进制输出
    # 这里打印形参 num 在函数内部的内存地址，验证它与外部实参是否指向同一个对象
    print("%d 在函数内的内存地址是 %x" % (num, id(num)))

    # 定义一个局部变量 result
    result = 100
    # 打印返回值 result 在函数内部的内存地址
    print("返回值 %d 在内存中的地址是 %x" % (result, id(result)))
    print("-" * 50)

    # 将 result 返回给调用者
    return result


# defines a variable 'a' with value 10
a = 10
# 打印调用函数前，变量 a 的内存地址
print("调用函数前 内存地址是 %x" % id(a))

# 调用 test 函数，传递实参 a，并将返回值赋值给变量 r
# 注意：传递的是 a 的引用（即 a 指向的内存地址）
r = test(a)

# 打印调用函数后，实参 a 的内存地址
# 对于整数这种不可变类型，函数内部的操作不会影响外部变量 a 的地址
print("调用函数后 实参内存地址是 %x" % id(a))

# 打印接收到的返回值 r 的内存地址
# 验证 r 的地址是否与函数内部 result 的地址一致
print("调用函数后 返回值内存地址是 %x" % id(r))
