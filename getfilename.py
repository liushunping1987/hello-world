#*******************************************************************
作者：final87
#*******************************************************************

import re
import os


def get_adam(dir_name):
    if os.path.exists(dir_name+'\\aa.txt'):
        os.remove(dir_name+'\\aa.txt')
    for filename in os.listdir(dir_name):
        if filename == '.idea' or filename == 'getfilename.py':
            continue
        file = open(dir_name+'\\'+filename, 'r')
        f = file.read()
        file.close()
        c = re.findall('(A.*?m).', f)
        fdp = open(dir_name+'\\'+'aa.txt', 'a+')
        for a in c:
            fdp.write(a+'\n')
        fdp.close()


def get_recursive_file_list(path):
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        print(file_name)
        full_file_name = os.path.join(path, file_name)
        print(full_file_name)
        all_files.append(full_file_name)
        print(all_files)

        if os.path.isdir(full_file_name):
            next_level_files = get_recursive_file_list(full_file_name)
            all_files.extend(next_level_files)

    return all_files


get_adam("F:\\python")
print(get_recursive_file_list(r'F:\test'))


