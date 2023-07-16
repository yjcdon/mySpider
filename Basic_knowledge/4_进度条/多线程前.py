import time
# 导入用于多线程操作的库
# 这样子仅需要在自定义的函数前面使用装饰器即可将函数开启新的线程
import multitasking
import signal
# 按快捷键 ctrl + c 终止已开启的全部线程
signal.signal(signal.SIGINT, multitasking.killall)



# 多线程装饰器
@multitasking.task
def say(number: int):
    print(number)
    time.sleep(0.5)


start_time = time.time()
for i in range(5):
    say(i)
# 等待全部线程执行完毕
multitasking.wait_for_tasks()
end_time = time.time()
print('耗时:', end_time-start_time, '秒')