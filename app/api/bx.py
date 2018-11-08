from flask import request, jsonify
from app.models import *
from app.api import api


# coding:utf-8
import urllib.parse
import urllib.request
import lxml
from bs4 import BeautifulSoup
import json
import os
import xlrd
import traceback
import pymysql
import re
import time
import random


# 建立数据库连接
conn = pymysql.connect(user='root', passwd='123456', host='127.0.0.1', db='handling',
                       use_unicode=True, charset="utf8")
cur = conn.cursor()
conn2 = pymysql.connect(user='root', passwd='123456', host='127.0.0.1', db='flask_datacenter',
                        use_unicode=True, charset="utf8")
cur2 = conn2.cursor()



# 获取access_token
def get_access_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=8HftbWTErMnW3slQ3EHaWf2g&client_secret=ATWExulFPKpSNXIQmRY9nAj0QUMyhsCD'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        bs_content = BeautifulSoup(content, 'lxml')
        json_data = json.loads(str(bs_content.text))
        print(json_data)
    pass


# 'access_token': '24.4dfc262888f802d339e1928871e3b8e7.2592000.1544257433.282335-14726430'
def baidu_lexer(text):
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?access_token=24.4dfc262888f802d339e1928871e3b8e7.2592000.1544257433.282335-14726430'

    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    data = {
        "text": text
    }
    endata = json.dumps(data).encode('GBK')
    # data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, headers=headers, data=endata)
    info = urllib.request.urlopen(req).read()
    info_return = BeautifulSoup(info, 'lxml').text
    info_json = json.loads(info_return)

    return info_json


# 获取平安保险
def get_pingan_baoxian():
    main_url = 'http://baoxian.pingan.com/index.shtml?inner_media=http://baoxian.pingan.com/baoxianfuwu/index.shtml-%E5%81%A5%E5%BA%B7%E4%BF%9D%E9%99%A9-%E5%B7%A6%E4%BE%A7%E8%8F%9C%E5%8D%95&tabIndex=1'
    get_main_web = urllib.request.urlopen(main_url).read()
    get_main_tran_web = BeautifulSoup(get_main_web, 'lxml').find(class_="proption fl ").contents
    for i in range(len(get_main_tran_web)):
        if i % 6 == 3 and i != 33:
            print(i, '#########################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#########################')
            all_bx_type = get_main_tran_web[i].find_all(class_="fc333")
            for j in range(len(all_bx_type)):
                one_bx_top = all_bx_type[j]
                if one_bx_top.has_attr('href'):
                    one_bx = one_bx_top.attrs
                    bx_title = one_bx['title']
                    bx_infourl = 'http://baoxian.pingan.com' + one_bx['href']
                    print(bx_title, bx_infourl)
                    cur.execute("insert into a平安保险(aa, bb) values (%s, %s)", [bx_title, bx_infourl])
                    conn.commit()


# 处理判断 关键词
def duel_keywords():



    pass


# 测试 随机一个的保险内容提取
def get_all_keys_info():
    url = 'http://baoxian.pingan.com/product/guoneilvyoubaoxianzzy.shtml'
    get_web = urllib.request.urlopen(url).read()
    get_tran_web = BeautifulSoup(get_web, 'lxml').find(id="page_Tab_cell2")
    bx_info_text = get_tran_web.text

    all_keys = []

    all_lines = bx_info_text.split('\n')
    for i in range(len(all_lines)):
        if all_lines[i] != '':
            one_line = all_lines[i]
            print(one_line)
            if '保险条款' in one_line:
                break
            else:
                juzi_info = baidu_lexer(one_line)
                juzi_text = juzi_info['text']
                juzi_items = juzi_info['items']
                # print(juzi_text, juzi_items)
                for j in range(len(juzi_items)):
                    one_item = juzi_items[j]
                    all_keys.append(one_item['item'])


    print(all_keys)
    dict = {}
    for key in all_keys:
        dict[key] = dict.get(key, 0) + 1
    print(dict)

# if 保险条款 break
# 关键字： 旅游，意外，健康，财产，企业
# 收益，年金，分红
# 保障期限：长期，终生
# 年龄：0-18， 18-60， 60-


    # # 保存文本
    # f = open("bx_info.txt", 'w', encoding='utf-8')
    # f.write(bx_info_text)
    # f.close()
    # # 读取文本
    # ff = open("bx_info.txt", 'r', encoding='utf-8')
    # ff.read()
    # lines = ff.readline()



get_all_keys_info()
