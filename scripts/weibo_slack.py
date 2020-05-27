from __future__ import unicode_literals
import base64
import logging
import sys
from datetime import datetime

from models.wbscrapper import WeiboLogin
from models.consts import WB_ACCOUNT, WB_PASSWD, FM_CHL, DONGXI_CHL

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

def main():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s\t%(levelname)s\t%(message)s")
    username = WB_ACCOUNT
    password = WB_PASSWD
    client = WeiboLogin(username=username,password=password)
    client.Login()

    #############################


    data = client.search('仇志飞')
    print(data)

    # config = CONFIG.get(product)
    # if not config:
    #     return

    # name = config['name']
    # keywords = config['keywords']
    # banwords = config['banwords']
    # dbkey_end_mid = config['dbkey']
    # maxpage = config['maxpage']




    #############################

if __name__ == '__main__':
    main()
    