#!/usr/env/bin python3.5
# -*-encoding:utf-8-*-
from bs4 import BeautifulSoup

def get_douban_comments(res):
    comments_list=[]
    soup = BeautifulSoup(res,'html.parser')
    comment_nodes=soup.select(".comment > p")
    for node in comment_nodes:
        comments_list.append(node.get_text().strip().replace("\n","") + u'\n')
    return comments_list



