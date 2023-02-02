import pandas as pd

f = open("result.txt",'r')
list_a = []
while True :
    line = f.readline()
    
    if not line : break
    print(line.split('    '))
    list_a.append(line.split('    '))

for k in list_a :
    print(k)
f.close()

classes = []
images = []
labels = []
precision = []
recall = []
mAp_5 = []
mAp_95 = []
df = pd.DataFrame()
# for k in s_list :
#     for j, con in enumerate(k) : 
        # classes.append(con[0])
        # images.append(con[1])
        # labels.append(con[2])
        # precision.append(con[3])
        # recall.append(con[4])
        # mAp_5.append(con[5])
        # mAp_95.append(con[6])
        # print(con)

# print(classes)
# for k in s_list :
#     print(k)
    
