# -*- coding: utf-8 -*-
# __author__="maple"
"""
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import jieba
from wordcloud import WordCloud
import os
import numpy
import PIL.Image as Image
from threading import Thread, Lock
from queue import Queue

cur_path = os.path.dirname(__file__)

from_file = os.path.join(cur_path, 'train/data.csv')
to_file = os.path.join(cur_path, "train/001.txt")

jieba.load_userdict(from_file)
LOCK = Lock()


def readfile(filepath, encoding='utf-8'):
    # 读取文本
    with open(filepath, "rt", encoding=encoding) as fp:
        content = fp.read()
    return content


def savefile(savepath, content):
    # 保存文本
    with open(savepath, "wt", encoding="utf-8") as fp:
        fp.write(content)


def check_dir_exist(dir):
    # 坚持目录是否存在，不存在则创建
    if not os.path.exists(dir):
        os.mkdir(dir)


def text_segment(from_file=from_file, to_file=to_file):
    content = readfile(from_file)
    print(content)
    seg_content = jieba.cut(content)
    savefile(to_file, ' '.join(seg_content))
    return True



stopwords = {'这些':0, '那些':0, '因为':0, '所以':0,'今天':0,'可能':0,'现在':0,'这个':0,'就是':0,'但是':0,'然后':0,} # 噪声词
mask_pic = numpy.array(Image.open(os.path.join(cur_path, 'train/love02.jpg')))
def chinese_jieba():
    with open(to_file, encoding='utf-8') as fp:
        txt = fp.read()
        # print(txt)
        wordcloud = WordCloud(
            # font_path = 'FZLTXIHK.TTF', # 字体
            font_path='msyh.ttc',  # 字体
            background_color='white',  # 背景色
            max_words=110,  # 最大显示单词数
            max_font_size=80,  # 频率最大单词字体大小60
            stopwords=stopwords,  # 过滤噪声词
            mask=mask_pic  # 自定义显示的效果图
        ).generate(txt)
        image = wordcloud.to_image()
        image.save('train/词云01.jpg')


if __name__ == '__main__':
    # text_segment(from_file,to_file)
    chinese_jieba()
