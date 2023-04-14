import os
import shutil
from tqdm import tqdm
def get_all_files_in_folder_v1(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # file_list.append(os.path.join(root, filename))
            file_list.append(filename)
    return file_list

def get_all_files_in_folder_v2(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_list.append(os.path.join(root, filename))
            # file_list.append(filename)
    return file_list

def copy_file(src_path, dst_path):
    try:
        # shutil.copy 함수를 사용하여 파일 복사
        shutil.copy(src_path, dst_path)
        print("File copied successfully.")
    except shutil.Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


lime_123_mix_test = get_all_files_in_folder_v1('/home/hwangbo/lime_mix/images/test')
lime_123_mix_val = get_all_files_in_folder_v1('/home/hwangbo/lime_mix/images/val')
lime_123_mix_train = get_all_files_in_folder_v1('/home/hwangbo/lime_mix/images/train')

print(len(lime_123_mix_test), len(lime_123_mix_val), len(lime_123_mix_train))
print(lime_123_mix_test[0])
lime_3_all = get_all_files_in_folder_v2('/home/hwangbo/showniq_4th_data/images/')
# lime_3_val = get_all_files_in_folder('/home/hwangbo/showniq_4th_data/images/val')
# lime_3_train = get_all_files_in_folder('/home/hwangbo/showniq_4th_data/images/train')


for k in tqdm(lime_3_all) :
    if k.split("/")[-1] in lime_123_mix_test :
        copy_file(k, '/home/hwangbo/lime_mix_3/images/test/' + k.split("/")[-1])
        labels_path = k.replace('images','labels_txt')
        labels_path = labels_path.replace('jpg','txt')
        copy_file(labels_path, '/home/hwangbo/lime_mix_3/labels/test/' + k.split("/")[-1].replace('jpg','txt'))
    elif k.split("/")[-1] in lime_123_mix_train :
        copy_file(k, '/home/hwangbo/lime_mix_3/images/train/' + k.split("/")[-1])
        labels_path = k.replace('images','labels_txt')
        labels_path = labels_path.replace('jpg','txt')
        copy_file(labels_path, '/home/hwangbo/lime_mix_3/labels/train/' + k.split("/")[-1].replace('jpg','txt'))
    elif k.split("/")[-1] in lime_123_mix_val :    
        copy_file(k, '/home/hwangbo/lime_mix_3/images/val/' + k.split("/")[-1])
        labels_path = k.replace('images','labels_txt')
        labels_path = labels_path.replace('jpg','txt')
        copy_file(labels_path, '/home/hwangbo/lime_mix_3/labels/val/' + k.split("/")[-1].replace('jpg','txt'))
        
        