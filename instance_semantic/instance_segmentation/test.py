# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 下午2:32
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : test.py
# @Software: PyCharm
import glob
import json

label_files = glob.glob("/home/luolu/Desktop/pore660/train2017/*.json")
for image_id, filename in enumerate(label_files):
    # print("filename:", filename)

    with open(filename) as f:
        data = json.load(f)

        # extract an element in the response
        for k in data:
            if k == 'shapes':
                # print(k)
                # print(data[k])
                for item in range(len(data[k])):

                    # print(item)
                    frame_array = []
                    # print("label:", data[k][item]['label'])
                    label_name = data[k][item]['label']

                    # print(type(data[k][item]['points']))
                    points_list = data[k][item]['points']
                    if len(points_list) <= 3:
                        print("len points_list:", len(points_list))
                        print("filename:", filename)
