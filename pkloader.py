from glob import glob
import pickle
from tqdm import tqdm
import shutil

def copy_all_file(file_list, new_path, lab_path):
    for src_path in tqdm (file_list):
        img_file = src_path.split("/")[-1].replace('txt','jpg')
        origin_file = src_path.replace("labels_txt","images")
        origin_file = origin_file.replace("txt","jpg")
        label_file = src_path.replace("images","labels_txt")
        label_file = label_file.replace("jpg","txt")
        label_file_name = label_file.split("/")[-1]
        # print(origin_file, new_path)
        shutil.copyfile(origin_file, new_path+"/"+img_file)
        shutil.copyfile(label_file, lab_path+"/"+label_file_name)
        # print(label_file)
        # break
        print("파일 {} 작업 완료".format(img_file)) # 작업한 파일명 출력

# pic_list = sorted(glob("/home/hwangbo/Human_claasify/*.pickle"))

pic_list = '/home/hwangbo/Human_claasify/NOT_HUMAN_valid.pickle'
# with open(pic_list[0], 'rb') as pk :
#     data = pickle.load(pk)
# with open('pk_dir/CP_test.pickle', "rb") as f :
#     data = pickle.load(f)

img_path = '/home/hwangbo/Not_Human/images/val'
lab_path = '/home/hwangbo/Not_Human/labels/val'
# for pic in pic_list :
print(pic_list)
with open(pic_list, 'rb') as pk :
    data = pickle.load(pk)

copy_all_file(data, img_path, lab_path)    
print(f' file_name : {pic_list}, length of data : {len(data)}')
    
        
# for file in data :
#     print(f'file = {file}')
# # print(data)