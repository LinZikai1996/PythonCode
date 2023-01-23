import os

import cv2
import imagehash
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
    if hash_diff >= 0.9:
        print(f"图片的相似度是 {format(hash_diff, '.0%')}")
        return True
    else:
        return False


def get_image_size_info(path):
    image = Image.open(path)
    return image.size
