#说明:在函数体中的path即为你的目标地址,在调用函数时,是makedir(path=目标地址)


import os
def makedir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExists = os.path.exists(os.path.join("path", path))
    if not isExists:
        print('系统中无该文件夹,创建的地址是:', path)
        # 创建文件夹
        os.makedirs(os.path.join("path", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("path", path))
        return True
    else:
        print(path, '该地址的文件夹已存在')
        os.chdir(os.path.join("path", path))
        return False