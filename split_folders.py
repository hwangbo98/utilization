import os 
from glob import glob
import shutil
from tqdm import tqdm
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
def get_file_list(dir): 
    file_list = [] 
    labels_list = []
    for root, dirs, files in os.walk(dir): 
        for file in files: 
            file_path = os.path.join(root,file)
            json_path = file_path.replace("images", "labels_txt")
            json_path = json_path.replace("jpg","txt")
            file_list.append(file_path)
            labels_list.append(json_path.split("/")[-1]) 

    return file_list
# image_files = glob("/home/hwangbo/lime_mix_all/images/*.jpg")
dir_path = '/home/hwangbo/showniq_5th_data/images'
image_files = get_file_list(dir_path)
images = [name.replace(".jpg", "") for name in image_files]
print(images)
train_names, test_names = train_test_split(images, test_size =0.3, 
random_state=42, shuffle=True)


val_names, test_names = train_test_split(test_names, test_size = 0.67, 
random_state=42, shuffle=True)



def batch_move_files(file_list, source_path, destination_path) :
    for file in tqdm(file_list) :
        image = file.split('/')[-1] + '.jpg'
        # txt = file.split('/')[-1] + '.json'
        txt = file.split('/')[-1] + '.txt'
        source_path_txt = file.replace("images", "labels_txt")
        destination_path_txt = destination_path.replace("images", "labels")
        shutil.copy(os.path.join(file + ".jpg"), destination_path)
        shutil.copy(os.path.join(source_path_txt + ".txt"), destination_path_txt)

    return
        

source_dir = "/home/hwangbo/showniq_5th_data/images"

test_dir =  "/home/hwangbo/lime_mix_4/images/test/"
val_dir =  "/home/hwangbo/lime_mix_4/images/val/"
train_dir =  "/home/hwangbo/lime_mix_4/images/train/"

os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(train_dir, exist_ok=True)

batch_move_files(train_names, source_dir, train_dir)
batch_move_files(test_names, source_dir, test_dir)
batch_move_files(val_names, source_dir, val_dir)