#headers,param -> json

import re

file_path = r"file.txt"
for line in open(file_path,'r'):
    line=line.replace("\n","")
    list1 = line.split(': ',1)
    try:
        new_str = ('"'+list1[0]+'"'+':'+'"'+list1[1]+'"'+',')
    except:
        break
    with open(file_path,'a') as f:
        f.writelines(new_str)
        f.write("\n")
    f.close()
