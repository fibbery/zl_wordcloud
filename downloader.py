#!/usr/env/bin python3.5
# -*-encoding:utf-8-*-
'''
get comment
'''
import requests


def download_page(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Cookie" : 'gr_user_id=c6f0d0c6-4cf2-4da9-95bb-f5b71124b1a4; viewed="25870705_2372267"; ll="118282"; bid=ZoSrG1mSRRw; _vwo_uuid_v2=73AE50EF7F3FBCE0A58A09DA419CBD68|2091697c2ca9c0173cc859db425e8f42; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1502178669%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DwruT_0PhcpJ277HV98JSOxqfgQGuJPu0dcSCWYMz5Q4VLz5QDvJWMuSUDTQ6-xWp82cZPi7rnO9WCHpO4Tqb4q%26wd%3D%26eqid%3Ddff462360002b86000000006594c6c96%22%5D; __utmt=1; ps=y; ue="568263091@qq.com"; dbcl2="57533908:gqQ8w3XBXMA"; ck=Wi09; __utma=30149280.1437917833.1470267410.1502175785.1502178670.23; __utmb=30149280.1.10.1502178670; __utmc=30149280; __utmz=30149280.1502171275.20.18.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.207631259.1498180766.1502175785.1502178681.6; __utmb=223695111.0.10.1502178681; __utmc=223695111; __utmz=223695111.1502178681.6.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _pk_id.100001.4cf6=c9fd61aec379cd0c.1498180765.5.1502178681.1502175888.; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0'
    }
    return requests.get(url, headers=header).content

