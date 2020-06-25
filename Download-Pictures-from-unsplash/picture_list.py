import os
with open(os.path.join(os.getcwd(),'picture_list.txt'),'wb') as f:
    f.writelines([(i+'\n').encode('utf-8') for i in os.listdir(r"Path to store pictures")])