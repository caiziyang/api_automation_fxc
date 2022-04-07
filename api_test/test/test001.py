# -*- coding: utf-8 -*-
# Script Name   : test001.py
# Author        : Caiziyang
# Time          : 2022/3/8 10:45
# Version       : 1.0.1
# Modifications : 
#
# Description   :

import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

text = open('geci.txt', 'r', encoding='utf-8').read()
# text = " Not Found"
# 将歌词剪开
cut_text = jieba.cut(text)
# 以空格拼接
res = ' '.join(cut_text)
# 生成词云
wc = WordCloud(
    font_path='simkai.ttf',  # 字体
    background_color='white',
    # scale=20,
    width=1000,
    height=800,
    max_font_size=50,
    mask=plt.imread("002.jpg"),  # 背景图片
    max_words=10000
)
wc.generate(res)
wc.to_file('res.png')
