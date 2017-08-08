#!/usr/env/bin python3.5
# -*-encoding:utf-8-*-
'''
进行分词以及绘制云词
'''
import codecs
import jieba
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS


def save_key_words():
    '''
    get key words from comments.txt
    :return:
    '''
    jieba.enable_parallel(4)
    with codecs.open("comments.txt", encoding="utf-8") as f:
        comment_words = f.read()
    cut_txt = " ".join(jieba.cut(comment_words))
    with codecs.open("cuttext.txt", "a", encoding="utf-8") as f:
        f.write(cut_txt)


def draw_word_cloud():
    with codecs.open("cuttext.txt", "r", encoding="utf-8") as f:
        text = f.read()
    bg_image = imread("catch_you.png")
    wc = WordCloud(
        font_path="华文仿宋.ttf",  # 防止中文乱码
        background_color="white",
        mask=bg_image,
        stopwords=STOPWORDS,
        max_font_size=40,
        min_font_size=4,
        max_words=2000)
    word_cloud = wc.generate(text)
    word_cloud.to_file("word_cloud.jpg")


draw_word_cloud()
