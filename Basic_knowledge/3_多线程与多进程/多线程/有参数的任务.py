'''
1.导入模块 threading
2.创建多线程对象:名称=threading.Thread(target=任务名,args=(参数,))
    如果只有一个参数,要多一个逗号;如果有多个参数,那么args中的顺序要和函数一致,且不用多一个逗号
3.启动线程,执行任务:名称.start()
'''
import threading
import time


def sing(num,name):
    for i in range(num):
        print(name,'在sing')
        time.sleep(1)


def dance(num):
    for i in range(num):
        print('我在dance')
        time.sleep(1)


if __name__ == '__main__':
    num = int(input('输入循环次数:'))
    start = time.time()

    st = threading.Thread(target=sing,args=(num,'lyj'))
    dt = threading.Thread(target=dance,args=(num,))
    st.start()
    dt.start()

    end = time.time()

    print('\n用时:', end - start, '秒')
