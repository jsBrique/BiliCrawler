# coding：utf-8
#简单爬取b站连载新番TOP
#作者：砖砖(Brick,Brique)
#纯属练手用的代码
import requests
import demjson
import json
import re
url = ''

wbdata = requests.get("https://s.search.bilibili.com/cate/search",
                    params={"callback":"jqueryCallback_bili_8",
                            "main_ver":"v3",
                            "search_type":"video",
                            "view_type":"hot_rank",
                            "order":"click",
                            "copy_right":"-1",
                            "cate_id":"33",
                            "page":"1",
                            "pagesize":"30",
                            "jsonp":"jsonp",
                            "time_from":"20180428",
                            "time_to":"20180505",
                            "_":"1525520603176"}
                      ).text
undata=wbdata.encode('utf-8').decode('unicode_escape')
print(undata)
#data=re.match('.*\\(([^\\(\\)]*)\\)',undata).group()
data=re.sub('jqueryCallback_bili_8\\(',"",undata,1)
data=re.sub('\\)',"",data,1)
data=re.sub('\r',"",data,1)
data=re.sub('\n',"",data,1)
regex = re.compile(r'\\(?![/u"])')
data = regex.sub(r"\\\\",data)
print(data)
jdata=json.loads(data)
news = jdata['result']

for n in news:
    title = n['title']
    aid = n['id']
    url = n['arcurl']
    play = n['play']
    date_time=n['pubdate']
    print(url, title, 'av'+str(aid),'播放量：'+str(play),'更新时间：'+str(date_time))
