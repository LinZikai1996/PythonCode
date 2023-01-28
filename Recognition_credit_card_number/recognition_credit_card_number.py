import cv2

# 信用卡数字识别
import numpy as np

from Util.folder_util import get_all_files_under_folder
from Util.image_util import show_img


def sort_contours(contour_list, method="left-to-right"):
    reverse = False
    i = 0
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # 找到最小外接矩形
    # cv2.boundingRect(img)这个函数可以获得一个图像的最小矩形边框一些信息，
    # 参数img是一个二值图像
    # 返回四个参数，左上角坐标，矩形的宽高，一般形式为：x, y, w, h
    minimum_circumscribed_rectangle_list = [cv2.boundingRect(c) for c in contour_list]

    # zip(*sorted(zip())), 可以以对两个迭代对象进行排序
    (contour_list, minimum_circumscribed_rectangle_list) = zip(
        *sorted(zip(contour_list, minimum_circumscribed_rectangle_list),
                key=lambda b: b[1][i], reverse=reverse))

    return contour_list, minimum_circumscribed_rectangle_list


def get_number_template(image, contour_list):
    contour_dict = {}
    for (index, contour) in enumerate(contour_list):
        (x, y, w, h) = cv2.boundingRect(contour)
        # 最小外接矩形范围
        minimum_circumscribed_rectangle = image[y:y + h, x:x + w]
        cv2.rectangle(image, (x, y), (x + w, y + + h), (0, 0, 255), 3)
        show_img("template", image)
        minimum_circumscribed_rectangle = cv2.resize(minimum_circumscribed_rectangle, (57, 88))

        contour_dict[index] = minimum_circumscribed_rectangle

    return contour_dict


def get_template_dict(image_path):
    # 读取模版
    print(f"读取模版 {image_path}")
    template_img = cv2.imread(image_path)
    show_img("template", template_img)

    # 转成灰度图
    template_gray_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    show_img("template gray", template_gray_img)

    # 二值图像
    # cv2.threshold()
    # 第一个参数是源图像，应该是灰度图,
    # 第二个参数是对图像进行分类的阈值,
    # 第三个参数是最大值，表示如果像素值大于（有时小于）阈值则要给出的值,
    # 第四个参数决定给出不同类型的阈值
    template_binary = cv2.threshold(template_gray_img, 10, 255, cv2.THRESH_BINARY_INV)[1]
    show_img("template binary", template_binary)

    # 计算轮廓
    # cv2.findContours()
    # 接受二值图，cv2.RETR_EXTERNAL 外轮廓检测， cv2.CHAIN_APPROX_SIMPLE 只保留终点坐标
    # 返回 list 每个元素是图像轮廓
    contours, hierarchy = cv2.findContours(template_binary,
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
    print(f"轮廓个数 ： {np.array(contours, dtype=object).shape}")

    # cv2.drawContours在图像上绘制轮廓
    # 第一个参数是指明在哪幅图像上绘制轮廓,
    # 第二个参数是轮廓本身，在Python中是一个list,
    # 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓,
    # 第四个参数指定颜色,
    # 第五个参数指定轮廓线的宽度，如果是-1（cv2.FILLED），则为填充模式
    cv2.drawContours(template_img, contours, -1, (0, 0, 255), 3)
    show_img("template", template_img)

    contours = sort_contours(contours)[0]

    return get_number_template(template_img, contours)


if __name__ == '__main__':
    img_list = get_all_files_under_folder(
        "/Volumes/mobile_hard_disk/project/PythonCode/Recognition_credit_card_number/resource/image")

    # 获取模版字典
    contours_dict = get_template_dict(img_list[len(img_list) - 1])
