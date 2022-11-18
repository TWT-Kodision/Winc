__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

#get current dir and join path
def get_current_dir(folder = 'cache'):
    current_dir = os.path.join(os.getcwd(), 'files', folder)
    return current_dir


#removes files from dir
def clear_dir(path):
    for file_name in os.listdir(path):
        os.remove(os.path.join(path, file_name)) #constructs path and removes the file

#makes dir or cleans it
def clean_cache():
    dir = get_current_dir()
    if os.path.isdir(dir): #check if dir exist
        clear_dir(dir)
    else:
        os.mkdir(dir)

#extract zip and place in cache
def cache_zip(zip_file, cache_path):
    zip_object = ZipFile(zip_file)
    zip_object.extractall(cache_path)

#put data to cache
def data_to_cache():
    zip_file = get_current_dir('data.zip')
    cache_path = get_current_dir()
    cache_zip(zip_file, cache_path)

#makes list of cached files
def cached_files():
    cache_path = get_current_dir()
    cache_list = []
    for file_name in os.listdir(cache_path):
        cache_list.append(os.path.join(cache_path, file_name))
    return cache_list

#find password in file list using a list
def find_password(file_list = cached_files()):
    password_indication = 'password'
    for file in file_list:
        file_content = open(file)
        content = file_content.read()
        if password_indication in content:
            password_raw = content[content.find(password_indication)+len(password_indication)+2:] #remove string before password
            password = password_raw[0:password_raw.find('\n')]  #remove lines after password
            return password
        file_content.close
