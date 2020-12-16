# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 上午11:00
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : split_files_with_ratio.py
# @Software: PyCharm

import glob
import os
import cv2
import errno
import shutil

# param need configure
# train val test [0:1]
div_ratio = [0.8, 0.1, 0.1]
file_path = "/home/luolu/Desktop/instance_dataset/particle_all/1/"
type_file = "*.json"
dst_path = "/home/luolu/Desktop/instance_dataset"

dst_train_path = dst_path + "/train"
dst_val_path = dst_path + "/val"
dst_test_path = dst_path + "/test"
# counter
train_counter = 0
val_counter = 0
test_counter = 0
if __name__ == '__main__':
    # get all json files
    json_Counter = len(glob.glob1(file_path, type_file))
    print("json_Counter:", json_Counter)
    num_train = int(json_Counter * div_ratio[0])
    num_val = int(json_Counter * div_ratio[1])
    num_test = int(json_Counter * div_ratio[2])
    print("num_train:", num_train)
    print("num_val:", num_val)
    print("num_test:", num_test)
    # make train val test dst dir
    try:
        os.makedirs(dst_train_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.makedirs(dst_val_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.makedirs(dst_test_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    #  cp file to dst path
    for json_file in glob.glob(file_path + "*.json"):
        png_file = json_file.split(".")[0] + ".png"
        # print(png_file)
        # src = json_file
        # dst = dst_*_path
        if train_counter < num_train:
            shutil.copy(json_file, dst_train_path)
            shutil.copy(png_file, dst_train_path)
            train_counter = train_counter + 1
            # print(json_file)
        elif val_counter < num_val:
            shutil.copy(json_file, dst_val_path)
            shutil.copy(png_file, dst_val_path)
            val_counter = val_counter + 1
            # print(json_file)
        elif test_counter < num_test:
            shutil.copy(json_file, dst_test_path)
            shutil.copy(png_file, dst_test_path)
            test_counter = test_counter + 1
            # print(json_file)
    print("train_counter:", train_counter)
    print("val_counter:", val_counter)
    print("test_counter:", test_counter)
