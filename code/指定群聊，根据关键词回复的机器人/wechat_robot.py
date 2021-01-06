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




# 堵塞线程，并进入 Python 命令行
# embed()
bot.join()
