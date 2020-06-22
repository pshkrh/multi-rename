import os
import logging

def add_affix(dir_path=None, affix=None, affix_type=None, sep='', filter_ext=[]):
    if dir_path is not None and affix is not None:
        if not dir_path.endswith(os.path.sep):
            dir_path += os.path.sep

        file_list = os.listdir(dir_path)

        for file_str in file_list:
            file_path = os.path.join(dir_path, file_str)
            file_name, extension = os.path.splitext(file_str)

            if filter_ext and extension[1:] in filter_ext:
                continue

            if not os.path.isdir(file_path):
                if affix_type == 'prefix':
                    repl_name = affix + sep + file_name + extension
                elif affix_type == 'suffix':
                    repl_name = file_name + sep + affix + extension
                
                repl_path = os.path.join(dir_path, repl_name)
                os.replace(file_path, repl_path)

def full_rename(dir_path=None, new_name=None, idx=1, increment=1, sep='', filter_ext=[]):
    if dir_path is not None and new_name is not None:
        if not dir_path.endswith(os.path.sep):
            dir_path += os.path.sep

        file_list = os.listdir(dir_path)

        for file_str in file_list:
            file_path = os.path.join(dir_path, file_str)
            extension = os.path.splitext(file_str)[1]

            if filter_ext and extension[1:] in filter_ext:
                continue

            if not os.path.isdir(file_path):
                repl_name = new_name + sep + str(idx) + extension
                repl_path = os.path.join(dir_path, repl_name)
                os.replace(file_path, repl_path)
                idx += increment