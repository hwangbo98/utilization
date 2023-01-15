from glob import glob

input_path = "/home/hwangbo/yolov7/k-fashion/images/train"
file_path = "/home/hwangbo/yolov7/k-fashion/train.txt"
image_files = glob(input_path+"/*.jpg")

fw = open(file_path, "w")
count = 0
for line in image_files :
    fw.write(line+'\n')
    count+=1
# print(count)
fw.close()