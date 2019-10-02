import os
import logging

def multi_renamer(dir_path=None, new_name=None, increment=1):

    if None not in (dir_path,new_name):
        file_list = os.listdir(dir_path)
        idx = 1
        for file in file_list:
            file_name = dir_path + os.path.splitext(file)[0] + os.path.splitext(file)[1]
            extension = os.path.splitext(file)[1]

            if '' not in (file_name, extension):
                repl_name = dir_path + new_name + str(idx) + extension
                try:
                    os.rename(file_name,repl_name)
                except:
                    logging.basicConfig(filename='batcher.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
                    logging.warning('The file {} already exists.'.format(file_name))
                finally:
                    idx += increment
    else:
        logging.info('Please refer to the usage documentation.')