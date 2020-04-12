import requests
import re
f = open('image_links3.txt')
i = 1
for line in f:
    try:
        line =  str(line)[1:]
        line = line[:-1]
        pattern = re.compile(r'\d+')
        result = pattern.findall(line)
        index = result[0]
        s = str(i).zfill(5)
        '''
        print('http://www.getchu.com{}'.format(line))
        print('http://www.getchu.com/soft.phtml?id={}'.format(index))
        '''
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36','referer': 'http://www.getchu.com/soft.phtml?id={}'.format(index)}
        buffer = requests.get('http://www.getchu.com{}'.format(line),headers=headers)
        with open("images/{}.jpg".format(s), 'wb') as fo:
            fo.write(buffer.content)
            fo.flush()
            i += 1
    except:
        print('one pic error!')
        i += 1
