from .base import Illustration2VecBase
from .chainer_i2v import ChainerI2V, make_i2v_with_chainer
chainer_available = True
'''
caffe_available = False


try:
    from .caffe_i2v import CaffeI2V, make_i2v_with_caffe
    caffe_available = True
except ImportError:
    pass

try:
    
    chainer_available = True
except ImportError:
    pass

if not any([caffe_available, chainer_available]):
    raise ImportError('i2v requires caffe or chainer package')
'''