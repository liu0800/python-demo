# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     word_cloud_beta3
   Description :
   Author :       86138
   date：          2019/1/28
-------------------------------------------------
   Change Activity:
                   2019/1/28:
-------------------------------------------------
"""
import os
from PIL import Image
import numpy as np
from wordcloud import WordCloud

if __name__ == '__main__':

    textname = os.listdir()[3]

    with open(textname,'r',encoding='utf-8') as f:
        text = f.read()

    mask = np.array(Image.open('mao.jpg'))

    wordcloud = WordCloud(mask=mask,background_color='white').generate(text)
    imag = wordcloud.to_image()
    imag.show()
    # imag.save('shakespear.png')
    # print('图片保存成功')