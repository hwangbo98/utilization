import os
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

# mypath = "/Users/kite/Desktop/new_folder/HGU/2022-2/SHOWNIQ/labeling/labels/etc/etc001/5am.saigon_All_Basic-Street_CSvhVWBF_uB-20220417033626-51.json"

# output  = glob.glob("/mnt/hdd3/showniq/Data/lime_mix_all/labels/*.json", recursive=True)
error_img = []
# file_list_py = [file for file in output if file.endswith(".json")]
# print(len(file_list_py))
# outpath = "./result/"
first_data = "/home/hwangbo/showniq_1st_data/labels" # 기존 폴더 경로
second_data = "/home/hwangbo/showniq_2nd_data/labels"
third_data = "/home/hwangbo/showniq_4th_data/labels"

# new_path = "/home/hwangbo/showinq/Data/lime_1_2_3/images" # 옮길 폴더 경로

file_list_1 = read_all_file(first_data)
file_list_2 = read_all_file(second_data)
file_list_3 = read_all_file(third_data)

total = []
total = file_list_1 + file_list_2 + file_list_3

# 확장자가 .txt인 파일을 삭제
for file_name in tqdm(total):
    if file_name.endswith(".txt"):
        # file_path = os.path.join(dir_path, file_name)
        os.remove(file_name)
        print(f"{file_name} 파일이 삭제되었습니다.")
    