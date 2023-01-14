import shutil
from glob import glob

train_txt = glob("lime_mid_cp/train/*.txt")
test_txt = glob("lime_mid_cp/test/*.txt")
val_txt = glob("lime_mid_cp/val/*.txt")

for i in train_txt :
    shutil.move(i, 'label/train')

for i in test_txt :
    shutil.move(i, 'label/test')

for i in val_txt :
    shutil.move(i, 'label/val')