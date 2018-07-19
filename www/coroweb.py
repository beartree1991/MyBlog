'''
 * @Author: beartree 
 * @Date: 2018-07-12 22:11:50 
 * @Last Modified by:   beartree 
 * @Last Modified time: 2018-07-12 22:11:50 
'''

import asyncio, os, inspect, logging, functions
from urllib import parse
from aiohttp import web
from apis import APIError

def get(path):
    '''
    Define decorator @get('/path')
    '''
