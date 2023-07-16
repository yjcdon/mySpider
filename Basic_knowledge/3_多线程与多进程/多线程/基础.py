'''
1.导入模块 threading
2.创建多线程对象:名称=threading.Thread(target=任务名)
3.启动线程,执行任务:名称.start()

在main中是主线程,你的线程对象指向的函数是子线程,当子线程执行完毕后主线程才结束
'''
import threading
import time


def sing():
    for i in range(3):
        print('我在sing')
        time.sleep(1)


def dance():
    for i in range(3):
        print('我在dance')
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    # sing()
    # dance()
    st = threading.Thread(target=sing)
    dt = threading.Thread(target=dance)
    st.start()
    dt.start()

    end = time.time()

    print('\n用时:', end - start, '秒')
