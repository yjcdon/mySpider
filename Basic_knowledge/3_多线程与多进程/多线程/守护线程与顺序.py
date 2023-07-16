import threading
import time

'''
你启动了一个进程,就会生成一个主线程 
因为主线程会等待所有子线程结束后,它才结束
所以可以在创建线程对象时加一个参数daemon=True,就可以在主线程结束后直接结束该子线程,
此外,多线程的执行顺序是被CPU调度的,与创建顺序无关
'''
def run():
    for i in range(8):
        print('work...')
        time.sleep(0.2)

if __name__ == '__main__':
    t=threading.Thread(target=run,daemon=True)
    t.start()

    time.sleep(1)
    print('主线程结束...')