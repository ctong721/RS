import os
import math
from PIL import Image, ImageDraw
import numpy as np
from skimage import feature as ft
from sklearn.externals import joblib


def getRegionImage(path, w_region, h_region, label, s_w, s_h, iszyb=True, step=10):
    _images = []
    _labels = []

    for img_name in os.listdir(path):
        if os.path.isfile(path + img_name):
            print(img_name)
            img_path = path + img_name
            img = Image.open(img_path)
            r_w, r_h = img.size
            print(w_region, h_region, s_w, s_h, step)
            img = img.convert('L')
            if iszyb:
                img = img.resize((s_w, s_h))
                _images.append(np.asarray(img, dtype='float64') / 256.)
                _labels.append(label)
                w_s = 1
                h_s = 1
            else:
                w_s = math.ceil(r_w / step)
                h_s = math.ceil(r_h / step)
                for h in range(h_s):
                    for w in range(w_s):
                        w0 = step * w
                        w1 = w_region + step * w
                        h0 = step * h
                        h1 = h_region + step * h
                        box = (w0, h0, w1, h1)
                        region = img.crop(box)
                        region = region.resize((s_w, s_h))
                        _images.append(np.asarray(region, dtype='float64') / 256.)
                        _labels.append(label)
    return _images, _labels, w_s, h_s


def getHOG(_images, _transform_sqrt):
    _x = []
    for image in _images:
        features = ft.hog(image,  # input image
                          orientations=9,  # number of bins
                          pixels_per_cell=(6, 6),  # pixel per cell
                          cells_per_block=(2, 2),  # cells per blcok
                          transform_sqrt=_transform_sqrt,  # power law compression (also known as gamma correction) DO NOT use this if the image contains negative
                          feature_vector=True,  # flatten the final vectors
                          visualise=False)  # return HOG map
        _x.append(features)
    return _x


def getRS(_path, _clf, _w, _h, _step):
    _c = 0
    regions = []
    _images, _labels, w, h = regionImage(_path, _w, _h, 0, 25, 25, False, _step)
    x_test = getHOG(_images, False)
    y = _clf.predict(x_test)
    y = np.reshape(y, [h, w])
    for r in range(h):
        for c in range(w):
            w0 = _step * c
            w1 = _w + _step * c
            h0 = _step * r
            h1 = _h + _step * r
            if y[r, c] == 1:
                regions.append([w0, h0, w1, h1])
                _c = _c + 1
    return _c, regions
