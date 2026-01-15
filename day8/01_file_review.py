# # 读取README文件的内容并打印到控制台
# file = open("README", encoding="utf-8")
#
# #  读取文件的全部内容
# text = file.read()
#
# print(text)
#
# file.close()

# f = open("README", "w")
#
# f.write("Hello, Python File Handling!\n")
# f.write("今天是2026年6月的一个美好日子。\n")
#
# f.close()

# 打开文件
# f = open("README")
#
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end="")  # end="" 避免重复换行
#
# f.close()


# # 打开文件
# file_read = open("README")
# file_write = open("README[副本]", "w")
#
# # 逐行读取并写入新文件
# text = file_read.read()
# file_write.write(text)
#
# # 关闭文件
# file_read.close()
# file_write.close()

# file_read = open("README")
# file_write = open("README[副本]", "w")

# # 逐行读取并写入新文件
# while True:
#     # 逐行读取
#     line = file_read.readline()
#
#     if not line:
#         break
#
#     file_write.write(line)

file = open('README','w+')
print(type(file))



file.write('123 hello')
file.seek(1)
text = file.read()
print(text)


file.close()




