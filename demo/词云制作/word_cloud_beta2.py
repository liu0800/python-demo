# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     word_cloud_beta2
   Description :
   Author :       86138
   date：          2019/1/26
-------------------------------------------------
   Change Activity:
                   2019/1/26:
-------------------------------------------------
"""

import os
from PIL import Image
import jieba
import numpy as np
from wordcloud import WordCloud

if __name__ == '__main__':

    with open('周杰伦.txt','r',encoding='utf-8') as f:
        text = f.read().replace(' ','').replace('\n','').strip()

    text = jieba.cut(text)
    text = ''.join(text)

    mask = np.array(Image.open('mao.jpg'))

    wordcloud = WordCloud(

        mask=mask,
        font_path="hanyinangong.ttf",
        background_color='white'
    ).generate(text)

    wordcloud.to_file('test.jpg')
