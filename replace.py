def replace_in_file(file_path, old_str, new_str) :
    fr = open(file_path, 'r')
    lines = fr.readlines()
    fr.close()


    fw = open(file_path, 'w') 
    for line in lines :
        fw.write(line.replace(old_str, new_str))
    fw.close()


replace_in_file("/home/hwangbo/yolov7/lime_data_copy/val.txt", "/home/hwangbo/yolov7/lime_data/", "/home/hwangbo/yolov7/lime_data_copy/")