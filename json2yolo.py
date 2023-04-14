
#-*- coding:utf-8 -*-
import os
from os import walk, getcwd
import json
import glob
from PIL import Image
from tqdm import tqdm

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
def read_all_file(path):
    output = os.listdir(path)
    file_list = []

    for i in tqdm(output):
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)

    return file_list

# mypath = "/Users/kite/Desktop/new_folder/HGU/2022-2/SHOWNIQ/labeling/labels/etc/etc001/5am.saigon_All_Basic-Street_CSvhVWBF_uB-20220417033626-51.json"

# output  = glob.glob("/home/hwangbo/lime_mix_all/labels/*.json", recursive=True)
error_img = []
# file_list_py = [file for file in output if file.endswith(".json")]
# print(len(file_list_py))
# outpath = "./result/"
first_data = "/home/hwangbo/showniq_5th_data/labels" # 기존 폴더 경로
# second_data = "/home/hwangbo/showniq_2nd_data/labels"
# third_data = "/home/hwangbo/showniq_4th_data/labels"

# new_path = "/home/hwangbo/showinq/Data/lime_1_2_3/images" # 옮길 폴더 경로

file_list_1 = read_all_file(first_data)
# file_list_2 = read_all_file(second_data)
# file_list_3 = read_all_file(third_data)

total = []
total = file_list_1 
# + file_list_2 + file_list_3

# json_backup ="/mnt/hdd3/showniq/Data/lime_mix_all/labels_txt/"

# wd = getcwd()
#list_file = open('%s_list.txt'%(wd), 'w')

""" Get input json file list """
# json_name_list = []
# for file in os.listdir(mypath):
#     if file.endswith(".json"):
#         json_name_list.append(file)
    
new_path = "/home/hwangbo/showniq_5th_data/labels_txt/"
""" Process """
for i in tqdm(total) :
    img_path  = i.replace("labels","images",1)
    img_path = img_path.rstrip(".json") + ".jpg"
    # txt_name = i.replace("labels", "labels_txt")
    txt_name = i.rstrip(".json") + ".txt"
    txt_file_name = txt_name.split("/")[-1]
    new_path = "/home/hwangbo/showniq_5th_data/labels_txt/"

    # print(txt_name)
    # print(img_path)
    # print(txt_name)
    with open(i) as f :
        json_object = json.load(f)
    new_path = new_path + txt_file_name
    # file_name = txt_name.split("/")
    # new_txt_name = json_backup+file_name[-1] 
    # split_txt = new_txt_name.split("/")
    # new_txt = ""
    # for i in range(len(split_txt)) :
    #     if i == len(split_txt) - 1 :
    #         break
    #     else :
    #         new_txt = new_txt + split_txt[i] +"/"
    # dir_path = os.path.dirname(new_path)
# dir_path = os.path.dirname(file_path)

# # 디렉토리가 존재하지 않으면 생성
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)
    #print(new_txt)
    # if not os.path.exists(new_path) :
    #     os.makedirs(new_path)
    print(new_path)
    txt_outfile = open(new_path, "w")
    # for i in json_object :
    #     print(i['human_info']['style'])


    # for value in json_object["human_info"][0]['bounding_box'] :
    #     print(value[0])

    # print(len(json_object['item_info']))
    for i in range(len(json_object['item_info'])):
        strings = json_object['item_info'][i]['item_id'].split(":")
        
        x1 = float(json_object["item_info"][i]['bounding_box']['lt_x'])
        y1 = float(json_object["item_info"][i]['bounding_box']['lt_y'])
        x2 = float(json_object["item_info"][i]['bounding_box']['rb_x'])
        y2 = float(json_object["item_info"][i]['bounding_box']['rb_y'])
        
        cls_num = int(strings[3]) - 1 #대분류 cls 번호
        if(cls_num>63) :
            print(txt_name +'\n')
        #print(i ,": ", "x1 : ", x1, "y1 : ", y1, "x2 : ", x2, "y2 : ", y2, "class_num : ",cls_num)

        xmin = min(x1,x2)
        xmax = max(x1,x2)
        ymin = min(y1,y2)
        ymax = max(y1,y2)
        try :
            im = Image.open(img_path)
            w = int(im.size[0])
            h = int(im.size[1])

            # print(w, h)
            # print(xmin, xmax, ymin, ymax)
            b = (xmin, xmax, ymin, ymax)
            bb = convert((w,h), b)
            #print(bb)
            
            txt_outfile.write(str(cls_num) + " " + " ".join([str(a) for a in bb]) + '\n')
        except :
            # print(f'error image : {img_path}')
            error_img.append(img_path)

print(f'error img = {error_img}')
