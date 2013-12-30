# -*- coding: utf-8 -*-
'''
Created on 2013年10月9日

@author: Administrator
'''

import urllib.request
import json
class weather:
    url = "http://m.weather.com.cn/data/101280101.html"
    def __init__(self, url="http://m.weather.com.cn/data/101280101.html"):
        self.url = url
    def readData(self):
        html = urllib.request.urlopen(self.url)
        data = html.read().decode("utf-8")
        return data     
        
if __name__ == "__main__":
    w = weather()
    data=w.readData()
    ss=json.loads(data)
    info=ss["weatherinfo"]
    print("城市：%s"%info["city"],"------时间%s"%info["date_y"],info["week"])
    print("温度：%s"%info["temp1"],"----",info["temp2"],"----",info["temp3"],"----",info["temp4"],"----",info["temp5"])
    print("天气：%s"%info["weather1"],"----",info["weather2"],"----",info["weather3"],"----",info["weather4"],"----",info["weather5"])
    print("风速：%s"%info["wind1"],"----",info["wind2"],"----",info["wind3"],"----",info["wind4"],"----",info["wind5"])
    print("今日穿衣指数：%s"%info["index"],info["index_d"])
    print("48小时穿衣指数：%s"%info["index48"],info["index48_d"])
