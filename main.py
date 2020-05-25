import i2v
from PIL import Image
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
<<<<<<< HEAD

img = Image.open("1.jpg")
print(illust2vec.estimate_plausible_tags([img], threshold=0.25))
=======
for i in range(1,38159):
    img = Image.open("{}.jpg".format())
    result = illust2vec.estimate_plausible_tags([img], threshold=0.25)
    result_dict = dict(result[0]['general'])
    print(wow)
    if '1girl' in result_dict:
        for key in result_dict:
>>>>>>> 3af026b1e19344a1339ef9698f5af53722efb1c8
