import os 
from glob import glob
import shutil
from tqdm import tqdm
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
image_files = glob("/mnt/hdd3/showniq/Data/lime_mix_all/images/*.jpg")

images = [name.replace(".jpg", "") for name in image_files]

train_names, test_names = train_test_split(images, test_size =0.3, 
random_state=42, shuffle=True)


val_names, test_names = train_test_split(test_names, test_size = 0.67, 
random_state=42, shuffle=True)



def batch_move_files(file_list, source_path, destination_path) :
    for file in tqdm(file_list) :
        image = file.split('/')[-1] + '.jpg'
        txt = file.split('/')[-1] + '.json'
        source_path_txt = source_path.replace("images", "labels")
        destination_path_txt = destination_path.replace("images", "labels")
        shutil.copy(os.path.join(source_path, image), destination_path)
        shutil.copy(os.path.join(source_path_txt, txt), destination_path_txt)

    return
        

source_dir = "/mnt/hdd3/showniq/Data/lime_mix_all/images/"

test_dir =  "/mnt/hdd3/showniq/Data/lime_1_2_3/images/test/"
val_dir =  "/mnt/hdd3/showniq/Data/lime_1_2_3/images/val/"
train_dir =  "/mnt/hdd3/showniq/Data/lime_1_2_3/images/train/"

os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(train_dir, exist_ok=True)

batch_move_files(train_names, source_dir, train_dir)
batch_move_files(test_names, source_dir, test_dir)
batch_move_files(val_names, source_dir, val_dir)