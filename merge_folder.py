import pickle
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
first_data = "/home/hwangbo/showniq_1st_data/images" # 기존 폴더 경로
second_data = "/home/hwangbo/showniq_2nd_data/images"
third_data = "/home/hwangbo/showniq_4th_data/images"

# new_path = "/home/hwangbo/showinq/Data/lime_1_2_3/images" # 옮길 폴더 경로

file_list_1 = read_all_file(first_data)
file_list_2 = read_all_file(second_data)
file_list_3 = read_all_file(third_data)

total = []
total = file_list_1 + file_list_2 + file_list_3

print(f'total lengths of file : {len(total)}')
new_path = "/home/hwangbo/lime_mix_all/images"
copy_all_file(total, new_path )

# with open('/home/hwangbo/Human_claasify/file_path.pickle', 'wb') as f :
#     pickle.dump(total, f, pickle.HIGHEST_PROTOCOL)
    

# copy_all_file(file_list, new_path)

print("=" * 40)
print("러닝 타임 : {}".format(time.time() - start_time)) # 총 소요시간 계산

