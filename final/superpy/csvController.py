import csv
import os
from datetime import date

def getDir(filename):
    dirPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),filename)
    return dirPath

def processFile(filename, action, line, newline = ""):
    dir_path = getDir(filename)
    with open(dir_path, action, newline = newline) as file:
        writer = csv.writer(file, delimiter="|", quotechar="|")
        writer.writerow(line)

def makeFile(file, column_name):
    try:
        filename = file
        first_row = column_name
        action = "w"
        processFile(filename, action, first_row)
    except NameError:
        print("filename not recognized")

def makeBoughtFile():
    makeFile("bought.csv", ["id","product_name","buy_date","buy_price","expiration_date"])

def makeSoldFile():
    makeFile("sold.csv", ["id","bought_id","sell_date","sell_price"])

def getDataList(filename):
    dataList = []
    dir_path = getDir(filename)
    with open(dir_path) as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            dataList.append(row)
        return dataList

def getRowIndex(data_list, SearchRow):
    for row in data_list:
        if SearchRow == row:
            return data_list.index(row)
        
    
def addToBought(id, product_name, buy_date, buy_price,expiration_date):
    filename = "bought.csv"
    action = "a"
    add_product = id, product_name, buy_date, buy_price, expiration_date
    processFile(filename, action, add_product)

def addToSold(id, bought_id, sell_date, sell_price):
    filename = "sold.csv"
    action = "a"
    sold_product = id, bought_id, sell_date, sell_price
    processFile(filename, action, sold_product)

def searchInList(index, searchword, list):
    found=[]
    for row in list:
        if row[index]==searchword:
            found.append(row)
    return found

def getProductById(fileName, bought_id, index = 0):
    data = getDataList(fileName)
    found = searchInList(index, bought_id, data)
    return found

def getSoldListBySoldId(sold_id):   
    file_name = "sold.csv"
    found = getProductById(file_name, sold_id)
    return found

def getSoldListByBoughtId(bought_id):
    file_name = "sold.csv"
    index = 1
    found = getProductById(file_name, bought_id, index)
    return found

def getBoughtListByBoughtId(bought_id):
    file_name = "bought.csv"
    found = getProductById(file_name, bought_id)
    return found