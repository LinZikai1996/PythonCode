import cv2
from matplotlib import pyplot as plt

from util.image_util import check_target_img_is_from_source_img_or_no, get_image_size_info


def test_check_target_img_is_from_source_img_or_no():
    source_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"
    source_path = f"{source_folder}source_img.png"
    target_path = f"{source_folder}target_img.png"
    img = cv2.imread(source_path)
    length, width = get_image_size_info(target_path)
    result, x, y = check_target_img_is_from_source_img_or_no(source_path=source_path, target_path=target_path)

    if result:
        cv2.rectangle(img, (x, y), (x + length, y + + width), (7, 249, 151), 2)
        print(f"找到图片 位置: x {str(x)}, y {str(y)}")
        plt.figure()
        plt.imshow(img, animated=True)
        plt.show()
    else:
        print("没找到")
