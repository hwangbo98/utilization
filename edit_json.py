import json

file_path = '/home/hwangbo/yolov7/runs/detect/exp59/labels/151511.json'

with open(file_path, "r", encoding = 'utf-8') as fp :
    read_path = json.load(fp)

print(len(read_path['item_info']))

