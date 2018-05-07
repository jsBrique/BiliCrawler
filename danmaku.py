#作者砖砖
#爬取B站弹幕并生成词云图
import requests
import re
import bs4
from xml.etree import ElementTree as ET
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

class DanmakuCrawler:
    def __init__(self):
        self.htmldata=''

    def get_cid(self,aid):
        self.htmldata=requests.get('https://www.bilibili.com/video/'+str(aid)).text
        print(self.htmldata)
        #print(self.htmldata)
        self.cid=re.search('(cid=)|(cid\":)\\d+',self.htmldata).group()
        self.cid=re.sub('cid=',"",self.cid)
        self.cid = re.sub('cid\":', "", self.cid)
        print(self.cid)

    def get_xml(self,save_path=''):
        self.danmaku_xml=requests.get("http://comment.bilibili.com/"+str(self.cid)+'.xml').text

        self.danmaku_xml=re.sub('<?xml version="1.0" encoding="UTF-8"?>','',self.danmaku_xml)
        #print(self.danmaku_xml)
        root = ET.XML(self.danmaku_xml)
        #print(root.tag, ":", root.attrib)  # 打印根元素的tag和属性
        str_danmaku=''
        for child in root:
            str_danmaku=str_danmaku+child.text+'\n'


        return str_danmaku

if __name__=='__main__':
    crl=DanmakuCrawler()
    crl.get_cid('av21520286')
    strd=crl.get_xml()
    print(strd)
    text_from_file_with_apath = strd

    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)

    my_wordcloud = WordCloud(width=1000,height=1000,background_color='white').generate(wl_space_split)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
