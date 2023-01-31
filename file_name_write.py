from glob import glob

input_path = "/mnt/hdd3/showniq/Data/lime_data_copy/images/test/"
file_path = "/mnt/hdd3/showniq/Data/lime_data_copy/test.txt"
image_files = glob(input_path+"/*.jpg")

fw = open(file_path, "w")
count = 0
for line in image_files :
    fw.write(line+'\n')
    count+=1
# print(count)
fw.close()