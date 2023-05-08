import csv
import os
from datetime import date

#get the current dir and put the filename on the end of dir
def get_dir(filename):
    dirPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),filename)
    return dirPath

#process the csv file
def process_file(filename, action, line, newline = ""):
    dir_path = get_dir(filename)
    try: 
        with open(dir_path, action, newline = newline) as file:
            writer = csv.writer(file, delimiter="|", quotechar="|")
            writer.writerow(line)
    except FileNotFoundError: 
        print("couldnt open the file")

#makes new file
def make_file(file, column_name):
        filename = file
        first_row = column_name
        action = "w"
        process_file(filename, action, first_row)

#makes a new bought_file
def make_bought_file():
    make_file("bought.csv", ["id","product_name","buy_date","buy_price","expiration_date"])

#makes a new sold_file
def make_sold_file():
    make_file("sold.csv", ["id","bought_id","sell_date","sell_price"])

#makes complete file with list, first item on the list becomes header
def make_custom_file(filename, item_list):
    make_file(filename, item_list[0])
    del item_list[0]
    for item in item_list:
        process_file(filename,'a', item)

#reads the data in file and returns it in a list
def get_data_list(filename):
    dataList = []
    dir_path = get_dir(filename)
    try:
        with open(dir_path) as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                dataList.append(row)
            return dataList
    except FileNotFoundError:
        print("couldnt open the file")

def get_highest_id(filename):
    product_list = get_data_list(filename)
    del product_list[0]
    id_list = []
    for id in product_list:
        id_list.append(id[0])
    return int(max(id_list))

#gets the row number in a list using a search
def get_row_index(data_list, search):
    for row in data_list:
        if search == row:
            return data_list.index(row)

#adds a (new) product to the bought list        
def add_to_bought(product_name, buy_date, buy_price, expiration_date):
    filename = "bought.csv"
    action = "a"
    id = get_highest_id(filename) + 1
    add_product = id, product_name, buy_date, buy_price, expiration_date
    process_file(filename, action, add_product)

#adds a product that is sold to the sold list
def add_to_sold(bought_id, sell_price, sell_date):
    filename = "sold.csv"
    action = "a"
    id = get_highest_id(filename) + 1
    sold_product = id, bought_id, sell_date, sell_price
    process_file(filename, action, sold_product)

#adds list to file
def add_to_file(filename, list):
    action = "a"
    for item in list:
        process_file(filename, action, item)
        
#used for a search in list from the bought or sold file
def search_in_list(index, searchword, list):
    found=[]
    for row in list:
        if row[index]==searchword:
            found.append(row)
    return found

#gets the product with a given id (used for a search in the sold file)
def get_product_by_id(fileName, bought_id, index = 0):
    data = get_data_list(fileName)
    found = search_in_list(index, bought_id, data)
    return found

#gets item from sold list by sold id 
def get_sold_list_by_sold_id(sold_id):   
    file_name = "sold.csv"
    found = get_product_by_id(file_name, sold_id)
    return found

#gets item from sold list by bought id
def get_sold_list_by_bought_id(bought_id):
    file_name = "sold.csv"
    index = 1
    found = get_product_by_id(file_name, bought_id, index)
    return found

#gets item from bought list by bought id
def get_bought_list_by_bought_id(bought_id):
    file_name = "bought.csv"
    found = get_product_by_id(file_name, bought_id)
    return found
