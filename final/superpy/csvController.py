import csv
import os
from datetime import date

def get_dir(filename):
    dirPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),filename)
    return dirPath

def process_file(filename, action, line, newline = ""):
    dir_path = get_dir(filename)
    with open(dir_path, action, newline = newline) as file:
        writer = csv.writer(file, delimiter="|", quotechar="|")
        writer.writerow(line)

def make_file(file, column_name):
    try:
        filename = file
        first_row = column_name
        action = "w"
        process_file(filename, action, first_row)
    except NameError:
        print("filename not recognized")

def make_bough_file():
    make_file("bought.csv", ["id","product_name","buy_date","buy_price","expiration_date"])

def make_sold_file():
    make_file("sold.csv", ["id","bought_id","sell_date","sell_price"])

#makes complete file with list, first item on the list becomes header
def make_custom_file(filename, item_list):
    make_file(filename, item_list[0])
    del item_list[0]
    for item in item_list:
        process_file(filename,'a', item)

def get_data_list(filename):
    dataList = []
    dir_path = get_dir(filename)
    with open(dir_path) as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            dataList.append(row)
        return dataList

def get_gow_index(data_list, SearchRow):
    for row in data_list:
        if SearchRow == row:
            return data_list.index(row)
        
    
def add_to_bought(id, product_name, buy_date, buy_price,expiration_date):
    filename = "bought.csv"
    action = "a"
    add_product = id, product_name, buy_date, buy_price, expiration_date
    process_file(filename, action, add_product)

def add_to_sold(id, bought_id, sell_date, sell_price):
    filename = "sold.csv"
    action = "a"
    sold_product = id, bought_id, sell_date, sell_price
    process_file(filename, action, sold_product)

def search_in_list(index, searchword, list):
    found=[]
    for row in list:
        if row[index]==searchword:
            found.append(row)
    return found

def get_product_by_id(fileName, bought_id, index = 0):
    data = get_data_list(fileName)
    found = search_in_list(index, bought_id, data)
    return found

def ge_sold_list_by_sold_id(sold_id):   
    file_name = "sold.csv"
    found = get_product_by_id(file_name, sold_id)
    return found

def get_sold_list_by_bought_id(bought_id):
    file_name = "sold.csv"
    index = 1
    found = get_product_by_id(file_name, bought_id, index)
    return found

def get_bought_list_by_bought_id(bought_id):
    file_name = "bought.csv"
    found = get_product_by_id(file_name, bought_id)
    return found