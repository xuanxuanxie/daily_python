import os
import re
from shutil import copy

path = "C:\\Users\\mhzxx\\Desktop\\domain\\domain1_bandpass_data"
list = os.listdir(path)

new_list = []

for i in list:
    if re.match('.*lowpass_magnitude',i) != None:
        new_list.append(i)


for data in new_list:
    a = os.path.split(path)
    save_dir = a[0]+"\\fudu"
    ori_path = path+"\\"+data
    copy(ori_path,save_dir)

print("ok")




        






    