import pandas as pd
import numpy as np
import os
import jieba.analyse
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
# import  PIL  # Python 中的图像处理模块，在本文中用以对图片进行处理。
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
STOPWORDS=['to','the','is','in','be']
def Gender_status(friends):
      df=pd.DataFrame(friends)
      #print(df.columns)
      sex_group=df.groupby(['sex'],as_index=True)['sex'].count()
      # print(sex_group.index)
      sex_group1=pd.Series(list(sex_group),index=['Unknow','Man','Female'])
      sex_group1.plot(kind='pie')
      plt.show()

def Places_stats(users):
      place = pd.DataFrame(users)
      place_group = place.groupby('province', as_index=True)['province'].count().sort_values(ascending=False)
      print(type(place_group)) #Series
      print(place_group)
      place_group.head(15).plot(kind='bar')
      plt.show()

def Signature_data(users):
      signature = users['signature']
      words = ''.join(signature)
      res_list = jieba.cut(words, cut_all=True)
      return res_list

def Create_wc(words_list):
      res_path = os.path.abspath('./static')
      words = ' '.join(words_list)
      back_pic = np.array(Image.open("%s/images/images.png" % res_path))
      stopwords = set(STOPWORDS)
      stopwords = stopwords.union(set(['class','span','emoji','emoji','emoji1f388','emoji1f604']))
      result = jieba.analyse.textrank(words, topK=1000, withWeight=True)
      # generate weight dictionary:
      keywords = dict()
      for i in result:
            keywords[i[0]] = i[1]
      wc = WordCloud(background_color="white", margin=0,
            font_path='%s/fronts/simhei.ttf' % res_path,
            mask=back_pic,
            max_font_size=70,
            stopwords=stopwords
            ).generate(words)
      # back_color = imread('./static/images/images.png')
      # image_colors = ImageColorGenerator(back_color)
      plt.imshow(wc)
      # plt.imshow(wc.recolor(color_func=image_colors))
      plt.axis('off')
      plt.title(u'My Weichat Key Words')
      plt.show()
      wc.to_file('%s/images/signatures.jpg' % res_path)


