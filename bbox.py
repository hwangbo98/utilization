import cv2
import json
import os
import glob
from tqdm import tqdm

img_path = "/home/hwangbo/yolov7/lime_data/images/test/americusgosani_Male_Basic-Gentleman_CYTUUcXhaQa-20220421064421-15.jpg"

json_path = "/home/hwangbo/Showniq_API/output/americusgosani_Male_Basic-Gentleman_CYTUUcXhaQa-20220421064421-15.json"

curr_path = os.getcwd()
file_list = sorted(glob.glob("/mnt/hdd3/split_lime/val" +"/**.jpg", recursive=True))
json_list = sorted(glob.glob("/home/hwangbo/Showniq_API/output/**.json", recursive=True))

# print(json_list)
for i, json_path in tqdm(enumerate(json_list)) :
     
    with open(json_path, "r") as fp :
        data = json.load(fp)

    bc = (255, 0, 0)
    gc = (0,255,0)
    # print(len(data["human_info"]))
    # print(f'length of human_info = {len(data["human_info"])}, human_info bbox = {data["human_info"][0]["bounding_box"]}' )

    img = cv2.imread(file_list[i],1)

    for k, human_box in enumerate(data["human_info"]) :
        lt_x = human_box["bounding_box"]["lt_x"]
        rb_x = human_box["bounding_box"]["rb_x"]
        lt_y = human_box["bounding_box"]["lt_y"]
        rb_y = human_box["bounding_box"]["rb_y"]
        # print(f'lt_x = {lt_x}, lt_y = {lt_y}, rb_x = {rb_x}, rb_y = {rb_y}')
        img =  cv2.rectangle(img,(lt_x,lt_y), (rb_x,rb_y), bc, 3)

    # print(print(f'length of item_info = {len(data["item_info"])}, item_info bbox = {data["item_info"][0]["bounding_box"]}' )
    # )
    for j, item_box in enumerate(data["item_info"]) :
        lt_x = item_box["bounding_box"]["lt_x"]
        lt_y = item_box["bounding_box"]["lt_y"]
        rb_x = item_box["bounding_box"]["rb_x"]
        rb_y = item_box["bounding_box"]["rb_y"]
        # print(f'lt_x = {lt_x}, lt_y = {lt_y}, rb_x = {rb_x}, rb_y = {rb_y}')
        img = cv2.rectangle(img,(lt_x, lt_y), (rb_x, rb_y), gc, 3)

    cv2.imwrite(curr_path + "/bbox_res/" + file_list[i].split('/')[-1].split('.')[0] + '.jpg', img)