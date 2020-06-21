import os
import logging

def full_rename(dir_path=None, new_name=None, idx=1, increment=1):

    if None not in (dir_path, new_name):
        if not dir_path.endswith(os.path.sep):
            dir_path += os.path.sep

        file_list = os.listdir(dir_path)

        for file_str in file_list:
            file_path = os.path.join(dir_path, file_str)
            extension = os.path.splitext(file_str)[1]

            if not os.path.isdir(file_path):
                repl_name = new_name + str(idx) + extension
                repl_path = os.path.join(dir_path, repl_name)
                os.replace(file_path, repl_path)
                idx += increment