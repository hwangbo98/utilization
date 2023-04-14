import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import time
import json
import glob
import pickle
import os
import shutil
import time
import pickle
from tqdm import tqdm

def read_all_file(path):
    output = os.listdir(path)
    file_list = []

    for i in (output):
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)

    return file_list

def copy_all_file(file_list, new_path):
    for src_path in tqdm (file_list):
        file = src_path.split("/")[-1]
        shutil.copyfile(src_path, new_path+"/"+file)
        print("파일 {} 작업 완료".format(file)) # 작업한 파일명 출력
        
        
# start_time = time.time() # 작업 시작 시간 
# first_data = "/home/hwangbo/showniq_1st_data/images" # 기존 폴더 경로
# second_data = "/home/hwangbo/showniq_2nd_data/images"
third_data = read_all_file("/home/hwangbo/showniq_5th_data/images")
# bc = (255,0,0)
print(len(third_data))
train_data = read_all_file("/home/hwangbo/lime_mix_all_1234/images/train")
only_file_train = [k.split("/")[-1] for k in train_data]
test_data = read_all_file("/home/hwangbo/lime_mix_all_1234/images/test")
only_file_test = [k.split("/")[-1] for k in test_data]
val_data = read_all_file("/home/hwangbo/lime_mix_all_1234/images/val")
only_file_val = [k.split("/")[-1] for k in val_data]
# with open('/home/youngchae/yolov7-face/data2.pickle','rb') as fp :
#     data = pickle.load(fp)

# for k in data[-35:-31] :
#     print(k[0])
# path = [
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303282336261001304919.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303282336261001304919.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303281822051001304705.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303281822051001304705.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303281822051001304705.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608051001296936.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608051001296936.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608051001296936.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608051001296936.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303281442091001304344.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303281442091001304344.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608141001296948.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608141001296948.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271608141001296948.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303272132191001299293.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303272132191001299293.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303272132191001299293.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/multiple/multiple001/202303271758101001297836.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/dresses/mini_dress/mini_dress001/202303291242051001304922.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/dresses/dress/dress001/202303281434181001304329.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/dresses/dress/dress001/202303281434181001304329.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/shoes/boots/boots001/202303271312071001295466.jpg",
#     "/home/hwangbo/showniq_5th_data/images/items/shoes/boots/boots001/202303271312131001295478.jpg"
# ]
file_list = ['202303211830051001294797.jpg', '202303271222201001295230.jpg', '202303271324061001295572.jpg',
             '202303271324111001295581.jpg', '202303271608141001296948.jpg', '202303271758101001297836.jpg',
             '202303281442091001304344.jpg', '202303281442171001304356.jpg', '202303281532131001304435.jpg',
             '202303281532151001304438.jpg', '202303281800171001304678.jpg', '202303281808081001304692.jpg',
             '202303281822231001304728.jpg', '202303282310051001304873.jpg']
# json_path = glob.glob('/home/hwangbo/Showniq_API/output/labels/**.json')
lines = []

with open("error_file_4th_data.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
        

path = list(set(lines))
with open("no_duplicate.txt", "w") as fp :
    for one in path :
        fp.write(one) 
        fp.write('\n')
# print(len(lines))
print(len(path))
count = 0
train_count = 0
val_count = 0
test_count = 0
save_list = []
# for jpg in path :
#     if jpg.split("/")[-1] in file_list :
#         count+=1
#         save_list.append(jpg.split("/")[-1])
#     # print(jpg.split("/")[-1])
for jpg in path :
    if jpg.split("/")[-1] in only_file_train :
        train_count+=1
        # save_list.append(jpg.split("/")[-1])
    elif jpg.split("/")[-1] in only_file_test :
        test_count+=1
    elif jpg.split("/")[-1] in only_file_val :
        val_count+=1
    # print(jpg.split("/")[-1])
# print(sorted(save_list))
print(f'train count : {train_count}, test count : {test_count}, val count : {val_count}')