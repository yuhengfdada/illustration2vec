import os
import requests
import re
f = open('out_links.txt')
fo = open('image_links.txt','a')

for line in f:
    try:
        print('processing '+str(line))
        source = requests.get('http://{}&gc=gc'.format(str(line)))
        content = source.text
        pattern = re.compile(r'\./brandnew[\S]+chara[\S]+\.jpg')   # 查找image link
        result = pattern.findall(content)
        if result:
            for link in result:
                fo.write(link+'\n')
    except:
        print('one pic error!')


