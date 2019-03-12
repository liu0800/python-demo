import os
from wordcloud import WordCloud

if __name__ == '__main__':

    textname = os.listdir()[2]

    with open(textname,'r',encoding='utf-8') as f:
        text = f.read()

    wordcloud = WordCloud().generate(text)

    imag = wordcloud.to_image()
    imag.show()
    imag.save('shakespear.png')


""""

2019年1月26日21:15:26

内容：
第一次使用python制作词云，这个只可以做英文版的，
而且不能替换蒙版，也就是说不能换背景图片，
中文 + 背景图片
见beta2

"""