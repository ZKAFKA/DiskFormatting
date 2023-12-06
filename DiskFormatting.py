import os
import random
import shutil
import stat


# 删除函数
def remove_file(dir_path):
    print("正在删除磁盘原有文件...")
    remove_dir_list = os.listdir(dir_path)
    for item in remove_dir_list:
        item_path = dir_path + "\\" + item
        if os.path.exists(item_path):
            if os.path.isdir(item_path):
                try:
                    shutil.rmtree(item_path)
                    print(item, '文件夹删除成功')
                except:
                    print(item, '文件夹删除失败！')
            elif os.path.isfile(item_path):
                try:
                    os.remove(item_path)
                    print(item, '文件删除成功')
                except Exception as e:
                    if 13 in e.args:
                        os.chmod(item_path, stat.S_IWUSR)
                        os.remove(item_path)
                        print(item, '文件删除成功')
                    else:
                        print("文件删除失败！")


if __name__ == '__main__':
    dir_path = input("请输入需要删除的磁盘路径（如C:）：")
    disk_size = input("请输入磁盘大小（单位Byte）：")
    disk_size = int(disk_size)
    remove_file(dir_path)
    print("已删除所有文件")

    disk = open(r'\\.\\'+dir_path, 'rb+')
    print(disk.read(disk_size))

    # 第一轮覆写 输入字符0x01
    print("第一轮：覆写字符 0x01")
    disk.seek(0)  # 将文件指针移回起始位置
    disk.write(b'\x01' * disk_size)

    # 第二轮覆写 输入字符0xff（01的补码）
    print("第二轮：覆写字符 0xff")
    disk.seek(0)
    disk.write(b'\xff' * disk_size)

    # 第三轮覆写 输入字符为随机值
    # 取随机数
    random_int = random.randint(1, 224)
    random_int = hex(random_int)
    padding = random_int.encode('utf-8')
    print("第三轮：覆写随机数字符 ", padding)
    disk.seek(0)
    disk.write(padding * disk_size)
    disk.seek(0)
    print("当前磁盘内数据：")
    print(disk.read(disk_size))

    disk.close()

