import os
import re


f = open('all_links.txt','rb')
fo = open('out_links.txt','a')
pattern = re.compile(r'www\.getchu\.com/soft\.phtml\?id=\d+')

for line in f:
    link = pattern.findall(str(line))
    fo.write(link[0]+'\n')

