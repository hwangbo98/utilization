import json
import argparse
from glob import glob
import shutil
from tqdm import tqdm
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
import os
import pickle

pickle_list = sorted(glob('/human.pickle'))

sum_data = 0
X_train = []
X_valid = []
X_test = []
for pk_name in pickle_list :
    with open(pk_name, "rb") as f:
        data = pickle.load(f)
        
        sum_data +=len(data)

# print(f'total = {sum_data}')

    train_names, test_names = train_test_split(data, test_size =0.3, 
random_state=42, shuffle=True)


    val_names, test_names = train_test_split(test_names, test_size = 0.66, 
random_state=42, shuffle=True)
    # y = np.zeros(len(data))
    print(f'pk_name = {pk_name}, train_count = {len(train_names)} ,valid_count = {len(val_names)}, test_count = {len(test_names)}')
    for train in train_names :
        X_train.append(train)
    for val in val_names :
        X_valid.append(val)
    for test in test_names :
        X_test.append(test)
    # X_train, X_temp, y_train, y_temp = train_test_split(data, y, test_size = 0.3, random_state = 42)
    # X_valid, X_test, _, _ = train_test_split(X_temp, y_temp, test_size = 0.66, random_state = 42)  

with open(os.path.join('HUMAN_train.pickle'), 'wb') as f:
    pickle.dump(X_train, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(os.path.join('HUMAN_valid.pickle'), 'wb') as f:
    pickle.dump(X_valid, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(os.path.join('HUMAN_test.pickle'), 'wb') as f:
    pickle.dump(X_test, f, protocol=pickle.HIGHEST_PROTOCOL)