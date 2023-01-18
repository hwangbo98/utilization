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
    

mypath = "/Users/kite/Desktop/new_folder/HGU/2022-2/SHOWNIQ/labeling/labels/etc/etc001/5am.saigon_All_Basic-Street_CSvhVWBF_uB-20220417033626-51.json"

output  = glob.glob("/mnt/hdd3/showniq/Data/lime_mix//**/*.json", recursive=True)

file_list_py = [file for file in output if file.endswith(".json")]
# print(file_list_py)
# outpath = "./result/"
json_backup ="/mnt/hdd3/showniq/Data/lime_mix/labels/"

wd = getcwd()
#list_file = open('%s_list.txt'%(wd), 'w')

""" Get input json file list """
# json_name_list = []
# for file in os.listdir(mypath):
#     if file.endswith(".json"):
#         json_name_list.append(file)
    

""" Process """
for i in tqdm(file_list_py) :
    img_path  = i.replace("labels","images",1)
    img_path = img_path.rstrip(".json") + ".jpg"
    txt_name = i.rstrip(".json") + ".txt"
    
    # print(img_path)
    # print(txt_name)
    with open(i) as f :
        json_object = json.load(f)
    file_name = txt_name.split("/")
    new_txt_name = json_backup+file_name[-1] 
    split_txt = new_txt_name.split("/")
    new_txt = ""
    for i in range(len(split_txt)) :
        if i == len(split_txt) - 1 :
            break
        else :
            new_txt = new_txt + split_txt[i] +"/"

    #print(new_txt)
    if not os.path.exists(new_txt) :
        os.makedirs(new_txt)
    txt_outfile = open(new_txt_name, "w")
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
            print(new_txt_name +'\n')
        #print(i ,": ", "x1 : ", x1, "y1 : ", y1, "x2 : ", x2, "y2 : ", y2, "class_num : ",cls_num)

        xmin = min(x1,x2)
        xmax = max(x1,x2)
        ymin = min(y1,y2)
        ymax = max(y1,y2)

        im = Image.open(img_path)
        w = int(im.size[0])
        h = int(im.size[1])

        # print(w, h)
        # print(xmin, xmax, ymin, ymax)
        b = (xmin, xmax, ymin, ymax)
        bb = convert((w,h), b)
        #print(bb)
        
        txt_outfile.write(str(cls_num) + " " + " ".join([str(a) for a in bb]) + '\n')
