import cv2
import json
import os
import glob
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description= 'Test for bounding box and waist')

# parser.add_argument('--dir_path', required=True, help='directory path')
# parser.add_argument('--json_path', required=True, help = 'json_path')

# img_path = "/home/hwangbo/1515.jpeg"

# json_path = "/home/hwangbo/output/1515.json"
# args = parser.parse_args()
# img_path = args.dir_path
# json_path = args.json_path
# json_path = '/home/hwangbo/output/'
# json_path += img_path.split('/')[-1].split('.')[0] +'.json'

# print(json_path)
curr_path = os.getcwd()
file_list = sorted(glob.glob("/mnt/hdd3/showniq/Data/lime_mix_all" +"/**.jpg", recursive=True))
json_list = sorted(glob.glob("/home/hwangbo/output/**.json", recursive=True))

# print(json_list)
for i, json_path in tqdm(enumerate(json_list)) : 
     
    with open(json_path, "r") as fp :
        data = json.load(fp)

    bc = (255, 0, 0)
    gc = (0,255,0)
    rc = (0, 0, 255)
    # print(len(data["human_info"]))
    # print(f'length of human_info = {len(data["human_info"])}, human_info bbox = {data["human_info"][0]["bounding_box"]}' )

    # img = cv2.imread(img_path,1)
    img = cv2.imread(file_list[i],1)

    for k, human_box in enumerate(data["human_info"]) :
        lt_x = human_box["bounding_box"]["lt_x"]
        rb_x = human_box["bounding_box"]["rb_x"]
        lt_y = human_box["bounding_box"]["lt_y"]
        rb_y = human_box["bounding_box"]["rb_y"]
        #### waist
        lf_waist_x = human_box["waist_points"]['lf_x']
        lf_waist_y = human_box["waist_points"]['lf_y']
        rh_waist_x = human_box["waist_points"]['rh_x']
        rh_waist_y = human_box["waist_points"]['rh_y']
        # print(f'lt_x = {lt_x}, lt_y = {lt_y}, rb_x = {rb_x}, rb_y = {rb_y}')
        img = cv2.rectangle(img,(lt_x,lt_y), (rb_x,rb_y), bc, 3)
        # img = cv2.putText(img, str(k), (lt_x,lt_y-10), cv2.FONT_HERSHEY_COMPLEX,0.6, gc, 1 )
        img = cv2.line(img, (rh_waist_x, rh_waist_y), (lf_waist_x, lf_waist_y), bc, 5)

    # print(print(f'length of item_info = {len(data["item_info"])}, item_info bbox = {data["item_info"][0]["bounding_box"]}' )
    # )
    for j, item_box in enumerate(data["item_info"]) :
        lt_x = item_box["bounding_box"]["lt_x"]
        lt_y = item_box["bounding_box"]["lt_y"]
        rb_x = item_box["bounding_box"]["rb_x"]
        rb_y = item_box["bounding_box"]["rb_y"]
        # print(f'lt_x = {lt_x}, lt_y = {lt_y}, rb_x = {rb_x}, rb_y = {rb_y}')
        img = cv2.rectangle(img,(lt_x, lt_y), (rb_x, rb_y), gc, 3)

    cv2.imwrite("/home/hwangbo/new_api/bbox_res/" + file_list[i].split('/')[-1].split('.')[0] + '.jpg', img)