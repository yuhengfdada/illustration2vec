# Illustration2Vec (an adaption by Yuheng)
## Description of i2v
``illustration2vec (i2v)`` is a simple library for estimating a set of tags and
extracting semantic feature vectors from given illustrations.
For details, please see
[our main paper](https://github.com/rezoo/illustration2vec/raw/master/papers/illustration2vec-main.pdf).
## Application by Yuheng
This repo, along with [this one](https://github.com/yuhengfdada/lbpcascade_animeface) records a full process of scraping images from a website, ordering them, cropping them to 128x128 and finally labelling them.  
It was a nice practice for:  
* Using external modules on github
* Overcoming anti-spider measures
* Washing data without any external modules (I used regular expression)
* Solving real-time problems
## Main project
This work is a part of my COMP4471 final project. [Check it out](https://github.com/yuhengfdada/ANIMEGAN).
# Requirements

* Pre-trained models (``i2v`` uses Convolutional Neural Networks. Please download
  several pre-trained models from
  [here](https://github.com/rezoo/illustration2vec/releases),
  or execute ``get_models.sh`` in this repository).
* ``numpy`` and ``scipy``
* ``PIL`` (Python Imaging Library) or its alternatives (e.g., ``Pillow``) 
* ``skimage`` (Image processing library for python)

In addition to the above libraries and the pre-trained models, `i2v` requires
either ``caffe`` or ``chainer`` library. If you are not familiar with deep
learning libraries, we recommend to use ``chainer`` that can be installed
via ``pip`` command.

# How to use

In this section, we show two simple examples -- tag prediction and the the
feature vector extraction -- by using the following illustration [1].

![slide](images/miku.jpg)

[1] Hatsune Miku (初音ミク), © Crypton Future Media, INC.,
http://piapro.net/en_for_creators.html.
This image is licensed under the Creative Commons - Attribution-NonCommercial,
3.0 Unported (CC BY-NC).

## Tag prediction

``i2v`` estimates a number of semantic tags from given illustrations
in the following manner.
```python
import i2v
from PIL import Image

illust2vec = i2v.make_i2v_with_chainer(
    "illust2vec_tag_ver200.caffemodel", "tag_list.json")

# In the case of caffe, please use i2v.make_i2v_with_caffe instead:
# illust2vec = i2v.make_i2v_with_caffe(
#     "illust2vec_tag.prototxt", "illust2vec_tag_ver200.caffemodel",
#     "tag_list.json")

img = Image.open("images/miku.jpg")
illust2vec.estimate_plausible_tags([img], threshold=0.5)
```

``estimate_plausible_tags()`` returns dictionaries that have a pair of
tag and its confidence.
```python
[{'character': [(u'hatsune miku', 0.9999994039535522)],
  'copyright': [(u'vocaloid', 0.9999998807907104)],
  'general': [(u'thighhighs', 0.9956372380256653),
   (u'1girl', 0.9873462319374084),
   (u'twintails', 0.9812833666801453),
   (u'solo', 0.9632901549339294),
   (u'aqua hair', 0.9167950749397278),
   (u'long hair', 0.8817108273506165),
   (u'very long hair', 0.8326570987701416),
   (u'detached sleeves', 0.7448858618736267),
   (u'skirt', 0.6780789494514465),
   (u'necktie', 0.5608364939689636),
   (u'aqua eyes', 0.5527772307395935)],
  'rating': [(u'safe', 0.9785731434822083),
   (u'questionable', 0.020535090938210487),
   (u'explicit', 0.0006299660308286548)]}]
```
These tags are classified into the following four categories:
*general tags* representing general attributes included in an image,
*copyright tags* representing the specific name of the copyright,
*character tags* representing the specific name of the characters,
and *rating tags* representing X ratings.

If you want to focus on several specific tags, use ``estimate_specific_tags()`` instead.
```python
illust2vec.estimate_specific_tags([img], ["1girl", "blue eyes", "safe"])
# -> [{'1girl': 0.9873462319374084, 'blue eyes': 0.01301183458417654, 'safe': 0.9785731434822083}]
```
# License
The pre-trained models and the other files we have provided are licensed
under the MIT License.
