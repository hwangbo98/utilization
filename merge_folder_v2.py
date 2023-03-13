import os 
import glob
from tqdm import tqdm
import shutil
import time

def get_file_list(dir): 
    file_list = [] 
    labels_list = []
    for root, dirs, files in os.walk(dir): 
        for file in files: 
            file_path = os.path.join(root,file)
            json_path = file_path.replace("images", "labels")
            json_path = json_path.replace("jpg","json")
            file_list.append(file_path)
            labels_list.append(json_path) 

    return file_list, labels_list

# def copy_all_file(file_list, new_path):
#     for src_path in tqdm (file_list):
#         file = src_path.split("/")[-1]
#         shutil.copyfile(src_path, new_path+"/"+file)
#         print("파일 {} 작업 완료".format(file)) # 작업한 파일명 출력
  
dir = '/home/hwangbo/showinq/Data/lime_3rd/labeling/images' # 디렉토리 이름 지정 
# new_file_path = "/home/hwangbo/showinq/Data/final_lime/images"
# new_json_path = "/home/hwangbo/showinq/Data/final_lime/labels"
file_list, json_list = get_file_list(dir) # 하위 디렉토리의 모든 파일을 리스트로 저장합니다.  

final = []
        
aaa = [k.split("/")[-1] for k in file_list] # 13,326개
bbb = [] #
result = []
for k in file_list :
    if k.split("/")[-1] in bbb :
        result.append(k)
    else :
        bbb.append(k.split("/")[-1])

print(f' error : {len(result)} bbb : {len(bbb)}')
print(result)

new = [a.split("/")[-1] for a in result] 
for j in file_list :
    if j.split("/")[-1] in new :
        final.append(j)

f = open("./error3.txt", 'w')
for i in range(len(final)):
    f.write(final[i]+'\n')
f.close()
print(f'length : {len(final)}')
# copy_all_file(file_list, new_file_path)
# copy_all_file(json_list, new_json_path)

file_output = glob.glob('/home/hwangbo/showinq/Data/final_lime/images/*.jpg')
json_output = glob.glob('/home/hwangbo/showinq/Data/final_lime/labels/*.json')

only_file = [k.split("/")[-1] for k in file_output ]
only_json = [k.split("/")[-1] for k in json_output ]

print(len(only_file), len(only_json))
print(len(file_list), len(json_list))

error_list = []
count = 0
an_count = 0
for i in file_list :
    # nur_file = i.split("/")[-1].split(".")[1]
    nur_file = i.split("/")[-1]
    # print(nur_file)
    if nur_file in only_file :
        count+=1
    else :
        an_count+=1
    # if nur_file in only_file :
    #     pass
    # elif nur_file not in only_file :
    #     print(i)
    #     error_list.append(i)
    # # if os.path.isdir(i) :
    #     count+=1
    

print(len(only_file))
print(count)
print(an_count)
print(error_list)