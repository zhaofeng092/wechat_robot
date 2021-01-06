# -*- coding: utf-8 -*-
# @Time : 2020/10/14 18:02
# @公众号 :Python自动化办公社区
# @File : rainbow.py
# @Software: PyCharm
# @Description:
# Q：不能登录网页版微信，怎么办？
# A：准确来说，目前无解
# Q：需要服务器吗？
# A：不需要，可以运行Python的电脑就可以。

from wxpy import *
import json
import random

# 机器人对象
bot = Bot()


# 辅助程序：随机获取彩虹屁语句
def get_random_line(file_name):
    group_file = file_name
    with open(group_file, encoding="utf-8") as f:
        data = json.load(f)
        sentence_id = random.randint(1, len(data))
    line = data[str(sentence_id)]
    return line


# 夸夸机器人主程序
@bot.register(Group, TEXT)
def print_group_msg(msg):
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        group_file = 'rainbow.json'
        line = get_random_line(group_file)
        print('你被@啦~，已回复：{}'.format(line))
        return '@{} {}'.format(msg.raw['ActualNickName'], line)


# 堵塞线程，并进入 Python 命令行
embed()
