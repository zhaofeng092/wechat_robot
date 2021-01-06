# 设置群昵称关键词，必填
robot_nick_name = '看门'  

#设置自动回复的对应关系，选填
keywords_reply = {
    '''对方说xxx''':'''你回复xxx''',
    '''''':'''''',
}

#密码
password = '123'

import hashlib
hl = hashlib.md5()
hl.update(password.encode(encoding='utf-8'))
correct_code= hl.hexdigest()
print(correct_code)
