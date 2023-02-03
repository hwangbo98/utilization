import os
import shutil
import time
from tqdm import tqdm

def read_all_file(path):
    output = os.listdir(path)
    file_list = []

    for i in tqdm(output):
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
        
        
start_time = time.time() # 작업 시작 시간 

src_path = "/home/hwangbo/labeling/labels/human/women" # 기존 폴더 경로
new_path = "/home/hwangbo/men_women/labels/women" # 옮길 폴더 경로

file_list = read_all_file(src_path)
copy_all_file(file_list, new_path)

print("=" * 40)
print("러닝 타임 : {}".format(time.time() - start_time)) # 총 소요시간 계산

