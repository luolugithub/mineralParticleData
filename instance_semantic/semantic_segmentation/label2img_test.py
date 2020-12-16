# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 上午9:26
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : label2img_test.py
# @Software: PyCharm
import imgviz
import cv2


label_path = "/home/luolu/PycharmProjects/labelme_src/examples/semantic_segmentation/mineral_labels.txt"
class_names = []
class_name_to_id = {}
for i, line in enumerate(open(label_path).readlines()):
    class_id = i - 1  # starts with -1
    class_name = line.strip()
    class_name_to_id[class_name] = class_id
    if class_id == -1:
        assert class_name == "__ignore__"
        continue
    elif class_id == 0:
        assert class_name == "_background_"
    class_names.append(class_name)
class_names = tuple(class_names)

label_img = cv2.imread("/home/luolu/Desktop/tmp_dataset/SegmentationClassPNG/bao1-16-1566_m002_s.png")
src_img = cv2.imread("/home/luolu/Desktop/tmp_dataset/JPEGImages/bao1-16-1566_m002_s.jpg")

print("label_img shape:", label_img.shape)
print("src_img.shape:", src_img.shape)
viz = imgviz.label2rgb(
                label=label_img,
                img=imgviz.rgb2gray(src_img),
                font_size=25,
                label_names=class_names,
                loc="rb",
            )
out_viz_file = "/home/luolu/Desktop/temp"
if __name__ == '__main__':

    imgviz.io.imsave(out_viz_file, viz)