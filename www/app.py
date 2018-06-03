# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 9:49
# @Author  : Beartree
# @FileName: app.py
# @Software: PyCharm

'''
logging不会抛出错误，而且可以输出到文件
它允许你指定记录信息的级别
有debug,info,warning,error等几个级别
'''
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime

# 基于asyncio实现的http框架，实现多用户的高并发支持
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine #异步io，可用async替代
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000) #yield from可用await替代
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()















