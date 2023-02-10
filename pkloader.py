from glob import glob
import pickle


pic_list = sorted(glob("/home/jinyoung/style/dataset/limeorange/*/*/*.pickle"  ))


with open(pic_list[0], 'rb') as pk :
    data = pickle.load(pk)
# with open('pk_dir/CP_test.pickle', "rb") as f :
#     data = pickle.load(f)

for file in data :
    print(f'file = {file}')
# print(data)