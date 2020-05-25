import os
import requests
import re
f = open('image_links2.txt')
fo = open('image_links3.txt','a')

for line in f:
    try:
        pattern = re.compile(r'\./brandnew[\S]+chara[\d]+\.jpg')   # 查找image link
        result = pattern.findall(line)
        if result:
            for link in result:
                fo.write(link+'\n')
    except:
        print('one pic error!')