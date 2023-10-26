import cv2
from PIL import Image, ImageChops
from matplotlib import pyplot as plt

from tool.image_util import check_target_img_is_from_source_img_or_no, get_image_size_info, screenshot, is_same_image


def test_check_target_img_is_from_source_img_or_no():
    source_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"
    source_path = f"{source_folder}source_img.png"
    screenshot(0, 0, 1560, 920, source_path)
    target_path = "/Volumes/mobile_hard_disk/project/PythonCode/Arknights/resource/image/have_potion_or_no.png"
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


def test_is_same_image():
    before_click_image_path = "resource/before_click.png"
    after_click_image_path = "resource/after_click.png"
    img1 = Image.open(before_click_image_path)
    img2 = Image.open(after_click_image_path)

    diff = ImageChops.difference(img1, img2)

    # 加强对比度
    diff = diff.point(lambda i: i * 5)

    # 如果需要，你还可以将差异与其中一个原始图像叠加，以便更清楚地看到差异
    highlighted_diff = ImageChops.add(img1, diff)

    # 保存高亮的差异图像
    highlighted_diff.save("resource/result.png")
