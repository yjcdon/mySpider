import threading
import time

'''
作用就是当你主线程完成后会进入阻塞状态,当子线程全部结束后,主线程才会结束
'''
def run():
    for i in range(10):
        print('work...')
        time.sleep(0.1)

if __name__ == '__main__':
    t=threading.Thread(target=run)
    t.start()
    t.join()
    time.sleep(0.5)
    print('主线程结束...')
