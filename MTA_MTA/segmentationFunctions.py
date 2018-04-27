from PIL import Image
import numpy as np
from skimage.filters import threshold_otsu
from skimage.measure import regionprops, label
from skimage.morphology import remove_small_objects


def segOtsu(img, minSize):
    thresh = threshold_otsu(img)
    imgOtsu = (img > thresh)
    imgOtsuFilt = remove_small_objects(imgOtsu, int(minSize))
    return imgOtsuFilt
