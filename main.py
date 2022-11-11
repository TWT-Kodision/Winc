__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

#removes files from dir
def clear_dir(path):
    for file_name in os.listdir(path):
        os.remove(f'{path}/{file_name}') #constructs path and removes the file

#makes dir or cleans it
def clean_cache():
    dir = 'files/cache'
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
    zip_file = 'files/data.zip'
    cache_path = 'files/cache'
    cache_zip(zip_file, cache_path)

#makes list of cached files
def cached_files():
    cache_path = os.path.abspath('files\cache')
    cache_list = []
    for file_name in os.listdir(cache_path):
        cache_list.append(f'{cache_path}\{file_name}')
    return cache_list

#find password in file list
def find_password(file_list):
    password_indication = 'password'
    for file in file_list:
        file_content = open(file)
        content = file_content.read()
        if password_indication in content:
            password_raw = content[content.find(password_indication)+len(password_indication)+2:] #remove string before password
            password = password_raw[0:password_raw.find('\n')]  #remove lines after password
            return password
        file_content.close
