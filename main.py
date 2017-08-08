#!/usr/env/bin python3.5
# -*-encoding:utf-8-*-
import downloader,comments_parser
import codecs
import random
import time

if __name__ == '__main__':
    templateurl='https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P'
    with codecs.open("comments.txt","a",encoding="utf-8") as f:
        for i in range(4249):
            print('开始爬取%d页评论...'%(i+1))
            targeturl = templateurl.format(i*20)
            res = downloader.download_page(targeturl)
            f.writelines(comments_parser.get_douban_comments(res))
            time.sleep(1 + float(random.randint(1,20))/20)





