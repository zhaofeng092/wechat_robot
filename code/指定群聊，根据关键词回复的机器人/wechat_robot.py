#!/usr/bin/env python3
# coding: utf-8

"""


登陆微信::

    # 导入模块
    from wxpy import *
    # 初始化机器人，扫码登陆
    bot = Bot()

找到好友::

    # 搜索名称含有 "游否" 的男性深圳好友
    my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]

发送消息::

    # 发送文本给好友
    my_friend.send('Hello WeChat!')
    # 发送图片
    my_friend.send_image('my_picture.jpg')

自动响应各类消息::

    # 打印来自其他好友、群聊和公众号的消息
    @bot.register()
    def print_others(msg):
        print(msg)

    # 回复 my_friend 的消息 (优先匹配后注册的函数!)
    @bot.register(my_friend)
    def reply_my_friend(msg):
        return 'received: {} ({})'.format(msg.text, msg.type)

    # 自动接受新的好友请求
    @bot.register(msg_types=FRIENDS)
    def auto_accept_friends(msg):
        # 接受好友请求
        new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，我自动接受了你的好友请求')

保持登陆/运行::

    # 进入 Python 命令行、让程序保持运行
    embed()

    # 或者仅仅堵塞线程
    # bot.join()


"""

import logging
import sys

from .api.bot import Bot
from .api.chats import Chat, Chats, Friend, Group, Groups, MP, Member, User
from .api.consts import ATTACHMENT, CARD, FRIENDS, MAP, NOTE, PICTURE, RECORDING, SHARING, SYSTEM, TEXT, VIDEO
from .api.consts import FEMALE, MALE
from .api.messages import Article, Message, Messages, SentMessage
from .exceptions import ResponseError
from .ext import Tuling, WeChatLoggingHandler, XiaoI, get_wechat_logger, sync_message_in_groups
from .utils import BaseRequest, detect_freq_limit, dont_raise_response_error, embed, ensure_one, mutual_friends

__title__ = 'wxpy'
__version__ = '0.3.9.8'
__author__ = 'Youfou'
__license__ = 'MIT'
__copyright__ = '2017, Youfou'

version_details = 'wxpy {ver} from {path} (python {pv.major}.{pv.minor}.{pv.micro})'.format(
    ver=__version__, path=__path__[0], pv=sys.version_info)

try:
    # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())


# -*- coding: UTF-8 -*-
from wxpy import *
import requests
import json
import time
import datetime
from config import robot_nick_name, keywords_reply,password

# 创建机器人
bot = Bot()
# bot = Bot(console_qr=-2, cache_path=True)  # 移植到linux，console_qr设置True和2都无法扫描登录,设置-2之后正常登录。

# 限定，只有群聊才回复
@bot.register(Group)
def print_messages(msg):
    # 群名称
    group_name = msg.sender.name
    # 处理群名称中含有的特殊符号
    while '#' in group_name:
        group_name = group_name.replace('#', 'woshiteshufuhao')
    # 登陆微信的用户群昵称
    user_name = msg.sender.self.name
    # 信息内容
    content = msg.raw['Content']
    # 发信息好友名称
    friend_name = msg.raw['ActualNickName']

    # 类型
    type = msg.raw['Type']
# 限定，只有群昵称中含有你设定的，才可以机器人回复
    if robot_nick_name in user_name:
        # insert(group_name, friend_name,type)
        print(msg)

def get_keywords(keywords_reply):
    keywords_reply.
    print(666)


# 堵塞线程，并进入 Python 命令行
# embed()
bot.join()
