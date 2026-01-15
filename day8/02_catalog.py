# import os
# import time
#
# try:
#     file_info = os.stat('README')
# except FileNotFoundError:
#     print("file.txt not found")
# else:
#     print(f"size: {file_info.st_size}, uid: {file_info.st_uid}, mode: {file_info.st_mode:#x}, mtime: {file_info.st_mtime}")
#     # 把秒数转为字符串时间（UTC）
#     print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(file_info.st_mtime)))

import os  # 必须导入os模块才能进行文件系统操作


def scan_dir(current_path, width):
    """
    深度优先遍历文件夹结构
    :param current_path: 当前正在扫描的文件夹绝对或相对路径
    :param width: 控制打印缩进的空格数量，代表当前的目录深度
    :return: None
    """
    # 1. 调用系统接口，获取指定路径下所有文件和子文件夹的名称列表
    file_list = os.listdir(current_path)

    # 2. 遍历列表中的每一个项目
    for file in file_list:
        # 3. 打印当前文件名。' ' * width 实现了层级缩进，让输出看起来像树状结构
        print(' ' * width, file)

        # 4. 路径拼接：将父目录路径与当前文件名组合，得到该项目的完整路径
        # 注意：手动用 '/' 拼接在不同系统间可能有兼容性问题，建议用 os.path.join()
        # 这种写法会自动根据你的系统（Windows 或 Linux）选择正确的斜杠
        new_path = os.path.join(current_path, file)

        # 5. 系统判断：检查这个完整路径指向的是不是一个“目录（文件夹）”
        if os.path.isdir(new_path):
            # 6. 递归调用：如果是文件夹，则“进入”该文件夹继续扫描
            # width + 4 代表子目录的内容要比父目录多缩进 4 个空格
            scan_dir(new_path, width + 4)


if __name__ == '__main__':
    # 从当前目录开始扫描，初始缩进宽度为 0
    scan_dir('.', 0)