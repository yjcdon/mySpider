import asyncio
import requests


# 使用async修饰的函数,调用后会返回一个协程对象
# async def fun(url):
#     print('hello:', url)
#
#
# # data为协程对象
# data = fun('www.baidu.com')
#
# # 创建事件循环对象,最好是这两行,不然有警告
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
#
# # 你要把协程对象 注册到 事件循环对象才能执行你的函数
# # loop.run_until_complete(data)
#
# # 使用task对象,它包含协程对象的各种状态
# task = loop.create_task(data)
# print(task)
# loop.run_until_complete(task)
# print(task)

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

#它不会调用函数
coro=main()

#执行函数内容:1.进入async模式;2.把coroutine变成task

# 1.进入async模式,建立event loop,event loop核心是有很多task,让它来决定哪个task来运行
asyncio.run(coro)
#然后用await来将coroutine object变成task,放回了event loop
