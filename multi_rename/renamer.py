import os
import logging

def add_affix(dir_path=None, affix=None, affix_type=None, sep='', filter_ext=[]):
    """Adds an affix to the existing file names in a directory

    Parameters
    ----------
    dir_path : str
        The directory which contains the files that need to be renamed
    affix: str
        The affix string which will be added to the existing
        file name
    affix_type: str
        The type of affix to be used. Possible values: prefix, suffix
    sep: str, optional
        Separator string to be used between the file name and affix
        (default is empty string)
    filter_ext : list of str, optional
        List of file extensions that should be ignored
        (default is an empty list)
    """

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
    """Renames all the files in a directory with a new name
    with incrementing numbers

    Parameters
    ----------
    dir_path : str
        The directory which contains the files that need to be renamed
    new_name: str
        The new name for all the files in the directory
    idx: int
        Start value of the trailing number for the file name
        (default is 1)
    increment: int
        The amount by which to increment the trailing number
        (default is 1)
    sep: str, optional
        Separator string to be used between the file name and affix
        (default is an empty string)
    filter_ext : list of str, optional
        List of file extensions that should be ignored
        (default is an empty list)
    """

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
