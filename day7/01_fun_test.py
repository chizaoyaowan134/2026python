# def mutable(num_list):
#     # num_list = [1, 2, 3]
#     num_list.extend([1, 2, 3])
#     print(num_list)
#
# if __name__ == '__main__':
#     gl_list = [6, 7, 8]
#     mutable(gl_list)
#     print(gl_list)
#


# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# # 需要将一个元组变量/字典变量传递给函数对应的参数
# gl_nums = (1, 2, 3)
# gl_xiaoming = {"name": "小明", "age": 18}
# # 会把 num_tuple 和 xiaoming 作为元组传递个 args
# # demo(gl_nums, gl_xiaoming)
# demo(*gl_nums, **gl_xiaoming)


def sum_numbers(num):
    print(num)
    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return
    sum_numbers(num - 1)

sum_numbers(3)
