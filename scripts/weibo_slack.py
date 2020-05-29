from __future__ import unicode_literals
import base64
import logging
import sys
from datetime import datetime

from models.wbscrapper import WeiboLogin
from models.consts import WB_ACCOUNT, WB_PASSWD, FM_CHL, DONGXI_CHL, DB_PATH, PRE_MID

import pickledb


path = sys.path[0] + '/' + DB_PATH
db = pickledb.load(path, False)

CONFIG = {
    'fm': {
        'name': u'豆瓣FM',
        'keywords': [u'豆瓣FM', u'豆瓣fm'],
        'banwords': [u'分享自 @豆瓣FM', u'来自@豆瓣FM',
                     u'来自豆瓣FM', u'豆瓣FM - Beta'],
        'dbkey': '/weibo/end_mid',
        'maxpage': 5,
        'logname': 'dae.collect.weibo',
        'channel': FM_CHL,
    },
    'dongxi': {
        'name': u'豆瓣东西',
        'keywords': [u'豆瓣东西'],
        'banwords': [],
        'dbkey': '/weibo/end_mid_dongxi',
        'maxpage': 5,
        'logname': 'dae.collect.weibo_dongxi',
        'channel': DONGXI_CHL,
    },
}


def get_msgs(product='fm'):
    config = CONFIG[product]
    if not config:

        return []

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s\t%(levelname)s\t%(message)s")
    username = WB_ACCOUNT
    password = WB_PASSWD
    client = WeiboLogin(username=username,password=password)
    client.Login()

    #############################

    name = config['name']
    keywords = config['keywords']
    banwords = config['banwords']
    dbkey_end_mid = config['dbkey']
    maxpage = config['maxpage']

    #############################

    data = []
    pre_pid = db.get(PRE_MID) or '0'

    for page in range(1, max_page + 1):
        result = client.search(name, page)
        if not result:
            break

        end = False
        for msg in result:
            if int(msg['mid']) > int(pre_pid):
                print(msg['text'])
                data.append(msg)
            else:
                end = True
                break
        if end:
            break
    
    if data:
        data.sort(key=lambda x: x['mid'])
        db.set(PRE_MID, data[-1]['mid'])
        db.dump()
    
    return data

def main():
    get_msgs()


    # data = client.search('王一博')
    # print(data)

    #############################

if __name__ == '__main__':
    main()
    