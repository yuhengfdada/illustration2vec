import i2v
from PIL import Image
import os
hair_list = ['blonde hair', 'brown hair', 'black hair', 'blue hair', 'pink hair' ,'purple hair', 'green hair','red hair', 'silver hair', 'white hair', 'orange hair', 'aqua hair', 'gray hair']
eye_list = ['blue eyes', 'red eyes', 'brown eyes' ,'green eyes', 'purple eyes', 'yellow eyes', 'pink eyes', 'aqua eyes', 'black eyes', 'orange eyes']
hairstyle_list = ['long hair','short hair', 'twintails', 'drill hair', 'ponytail']
other_list = ['blush', 'smile','open mouth', 'hat', 'ribbon', 'glasses']
illust2vec = i2v.make_i2v_with_chainer(
    "illust2vec_tag_ver200.caffemodel", "tag_list.json")

# In the case of caffe, please use i2v.make_i2v_with_caffe instead:
# illust2vec = i2v.make_i2v_with_caffe(
#     "illust2vec_tag.prototxt", "illust2vec_tag_ver200.caffemodel",
#     "tag_list.json")

output = {}

#output is a dictionary in the format like:
#{"1.image" : ["blonde hair", "blue eyes", "long hair", "smile"], 
# "2.image" : ["brown hair", "green eyes", "short hair", "ribbon"]}
count = 0
for i in range(1,37885):
    try:
        s = str(i).zfill(5)
        img = Image.open("../lbpcascade_animeface/examples/cropped/{}.jpg".format(s))
        result = illust2vec.estimate_plausible_tags([img], threshold=0.25)
        result_dict = dict(result[0]['general'])
        #print(result_dict)
        if '1girl' in result_dict:
            count += 1
            print('find girl')
            hair = None
            p = 0
            for j in hair_list:
                if result_dict.get(j, 0) > p:
                    hair = j
                    p = result_dict[j]
            lableList = [hair]
            
            eye = None
            p = 0
            for j in eye_list:
                if result_dict.get(j, 0) > p:
                    eye = j
                    p = result_dict[j]
            lableList.append(eye)

            hairstyle = None
            p = 0
            for j in hairstyle_list:
                if result_dict.get(j, 0) > p:
                    hairstyle = j
                    p = result_dict[j]
            lableList.append(hairstyle)

            for j in other_list:
                if j in result_dict:
                    lableList.append(j)
            
            output.update({"{}.jpg".format(s) : lableList})
        else:
            print('not a girl!')
            os.remove("../lbpcascade_animeface/examples/cropped/{}.jpg".format(s))
    except:
        print('one pic error!')


#The name of the output file
filename = "labels2.txt"
f = open(filename, "a")

print(count, file = f)

for i in hair_list:
    print(i.replace(' ','_'), end = ' ', file = f)
for i in eye_list:
    print(i.replace(' ','_'), end = ' ', file = f)
for i in hairstyle_list:
    print(i.replace(' ','_'), end = ' ', file = f)
for i in other_list:
    print(i.replace(' ','_'), end = ' ', file = f)
print('',file=f)

try:
    count = 0
    for i in range(1, 38159):
        s = str(i).zfill(5)
        imageName = "{}.jpg".format(s)
        if imageName in output:
            print('in output!')
            count += 1
            ss = str(count).zfill(5)
            print("{}.jpg".format(ss), end = " ", file = f)
            
            for j in hair_list:
                if j in output.get(imageName):
                    print("1", end = " ", file = f)
                else:
                    print("-1", end = " ", file = f)
            
            for j in eye_list:
                if j in output.get(imageName):
                    print("1", end = " ", file = f)
                else:
                    print("-1", end = " ", file = f)

            for j in hairstyle_list:
                if j in output.get(imageName):
                    print("1", end = " ", file = f)
                else:
                    print("-1", end = " ", file = f)

            for j in other_list:
                if j in output.get(imageName):
                    print("1", end = " ", file = f)
                else:
                    print("-1", end = " ", file = f)
            print('', file=f)
except:
    print('one pic error!')
f.close()
