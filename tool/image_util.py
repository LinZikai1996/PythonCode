import math
import os

import cv2
import imagehash
import numpy as np
from PIL import ImageGrab, Image


def screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, path):
    if os.path.exists(path):
        os.remove(path)
    ImageGrab.grab((left_top_x, left_top_y, bottom_right_x, bottom_right_y)).save(path)
    img = cv2.imread(path, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, gray)


def check_image_similarity(source_path, target_path):
    source_img = imagehash.average_hash(Image.open(source_path), hash_size=6)
    target_img = imagehash.average_hash(Image.open(target_path), hash_size=6)

    hash_diff = 1 - (target_img - source_img) / len(target_img.hash) ** 2
    if hash_diff >= 0.8:
        print(f"图片的相似度是 {format(hash_diff, '.0%')}")
        return True
    else:
        return False


def check_target_img_is_from_source_img_or_no(source_path, target_path):
    source_img = cv2.imread(source_path)  # 要找的大图
    source_img = cv2.resize(source_img, (0, 0), fx=1, fy=1)

    template_img = cv2.imread(target_path)  # 图中的小图
    template_img = cv2.resize(template_img, (0, 0), fx=1, fy=1)

    x, y = search_return_point(source_img, template_img)

    if x is None and y is None:
        return False, None, None
    else:
        return True, x, y


def search_return_point(source_img, template_img):
    source_img_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
    template_img_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(source_img_gray, template_img_gray, cv2.TM_CCOEFF_NORMED)

    # res大于70%
    loc = np.where(result >= 0.7)
    points = zip(*loc[::-1])

    x = 0
    y = 0
    index = 0
    for pt in points:
        x = x + int(pt[0])
        y = y + int(pt[1])
        index = index + 1
    if x != 0 and y != 0:
        return math.floor(x / index), math.floor(y / index)
    else:
        return None, None


def get_image_size_info(path):
    image = Image.open(path)
    return image.size


def show_img(name: str, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(image, height_size=None, width_size=None):
    # 获取原始图像宽高。
    height, width = image.shape[0], image.shape[1]

    if height_size:
        scale = height / height_size
    elif width_size:
        scale = width / width_size
    else:
        return None
    # 等比例缩放尺度。
    height = int(height / scale)
    # 获得相应等比例的图像宽度。
    width = int(width / scale)
    # resize
    return cv2.resize(image, (width, height))


def bgr_to_rgb(image):
    B, G, R = cv2.split(image)
    return cv2.merge([R, G, B])
