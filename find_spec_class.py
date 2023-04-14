import glob

img_1_data = glob.glob('/home/hwangbo/showniq_1st_data/images/items/swimwear/beach_tops/beach_tops001/*')
img_2_data = glob.glob('/home/hwangbo/showniq_2nd_data/images/items/swimwear/beach_tops/beach_tops001/*')
img_3_data = glob.glob('/home/hwangbo/showniq_4th_data/images/items/swimwear/beach_tops/beach_tops001/*')

total = img_1_data + img_2_data + img_3_data
train_data = glob.glob('/home/hwangbo/lime_mix/images/train/*')
new_train_data = [j.split("/")[-1] for j in train_data ]
print(new_train_data)
for k in total :
    if k.split("/")[-1] in new_train_data :
        pass
    else :
        print(k)