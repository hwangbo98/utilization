import os 
from glob import glob
import shutil
from tqdm import tqdm
import json
import argparse

parser = argparse.ArgumentParser(description="source & destination file path")

parser.add_argument("--json", required=True, help = 'json directory path')
parser.add_argument("--origin_img", required=True, help = 'image directory path')
parser.add_argument("--dest_img", required=True, help = 'destination directory path')

json_path = parser.json #"/home/hwangbo/new_api/output"
img_path =  parser.origin_img #"/mnt/hdd3/showniq/Data/lime_mix_all"
dest_path = parser.dest_img

json_list = glob(json_path + "/*.json")


for k, json in tqdm(json_list) :
    with open(json, "r") as fp :
        contents = json.load(fp)

    file_name = json.split("/")[-1].split(".")

    origin_img_name = img_path + file_name + ".jpg"
    dest_img_name = dest_path + file_name + ".jpg"
    if len(contents["human_info"]) == 0 :
        dest_img_name = dest_path + "zero_person/" + file_name + ".jpg"
        if not os.dest_img_name.isdir() :
            os.makedirs(dest_img_name) #폴더가 없으면 만들어주기
        shutil.copy(origin_img_name, dest_img_name)
    elif len(contents["human_info"]) == 1 :
        dest_img_name = dest_path + "single_person/" +file_name + ".jpg"
        if not os.dest_img_name.isdir() :
            os.makedirs(dest_img_name) #폴더가 없으면 만들어주기
        shutil.copy(origin_img_name, dest_img_name)
    else :
        dest_img_name = dest_path + "multi_person/" + file_name + ".jpg"
        if not os.dest_img_name.isdir() :
            os.makedirs(dest_img_name) #폴더가 없으면 만들어주기
        shutil.copy(origin_img_name, dest_img_name)



