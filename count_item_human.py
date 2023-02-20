import glob
from tqdm import tqdm

path_1 = glob.glob('/mnt/hdd3/showniq/Data/lime_1st/labeling/images/human/**/*.jpg', recursive=True)
path_2 = glob.glob('/mnt/hdd3/showniq/Data/lime_2nd/labeling/images/human/**/*.jpg', recursive=True)

# path_1 += path_2
assemble_path = path_1 + path_2
# print(assemble_path[:3])
print(len(assemble_path))
f = open('/home/hwangbo/showinq/Data/lime_mix/train.txt', 'r') 
f_list = []
while True :
    line = f.readline()
    if not line :
        break
    f_list.append(line.strip())

print(len(f_list))

# item = open('/home/hwangbo/showinq/Data/lime_mix/test_item.txt', 'r') 
# item_list = []
# while True :
#     line = item.readline()
#     if not line :
#         break
#     item_list.append(line.strip())

# for k in f_list :
#     if k not in item_list :
#         with open("/home/hwangbo/showinq/Data/lime_mix/test_human.txt", "a") as fp :
#             fp.write(k + "\n")
# # for line in f :
# #     print(f.split("/")[-1])
# #     break
count_item = 0
count_human = 0
for data in tqdm(assemble_path) :
    origin_path = "/mnt/hdd3/showniq/Data/lime_mix/images/train/"
    file_name = data.split("/")[-1]
    new_path = origin_path + file_name

    if (new_path in f_list) :
        # with open("/home/hwangbo/showinq/Data/lime_mix/test_item.txt", "a") as file :
        #     file.write(new_path + "\n")
        count_human+=1
    # else :
    #     count_human+=1

print(f'include human : {count_human}, only item : {len(f_list)-count_human}')
    # else :
    #     with open("/home/hwangbo/showinq/Data/lime_mix/test_human.txt", "a") as fp :
    #         fp.write(new_path + "\n")

# with open("/home/hwangbo/showinq/Data/lime_mix/test.txt", "r") as file :
#     strings = file.readlnes()
# print(strings)
# while True :
#     line = f.readline()
#     origin_path = "/mnt/hdd3/showniq/Data/lime_mix/images/test/"
#     if not line : break
#     file_name = line.split("/")[-1]
#     new_path = origin_path + file_name

#     if ((assemble_path.split("/")[-1] == file_name)) :
#         with open("/home/hwangbo/showinq/Data/lime_mix/test_item.txt", "a") as file :
#             file.write(new_path)
#     else :
#         with open("/home/hwangbo/showinq/Data/lime_mix/test_human.txt", "a") as fp :
#             fp.write(new_path)

    # if file_name  