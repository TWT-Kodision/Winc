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

def makeFile(file):
    try:
        if file == "bought":
            line = "id", "product", "product_name", "buy_date", "expiration_date", "amount"
            filename = "bought.csv"
           
        elif file == "sold":
            line = "id", "product", "product_name", "buy_date", "expiration_date", "amount"
            filename = "sold.csv"

        action = "w"
        processFile(filename, action, line)
    except NameError:
        print("filename not recognized")

def getDataList(filename):
    dataList = []
    dir_path = getDir(filename)
    with open(dir_path) as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            dataList.append(row)
        print(dataList) 
        return dataList

def getRowIndex(data_list, SearchRow):
    for row in data_list:
        if SearchRow == row:
            return data_list.index(row)
        
def addToBought(id, product, product_name, buy_date, expiration_date, amount):
    filename = "bought.csv"
    action = "a"
    add_product = id, product, product_name, buy_date, expiration_date, amount
    processFile(filename, action, add_product)

def addToSold(id, bought_id, sell_date, sell_price, amount_sold):
    filename = "sold.csv"
    action = "a"
    sold_product = id, bought_id, sell_date, sell_price, amount_sold
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

    
makeFile("bought")
makeFile("sold")
addToBought("12", "test", "name", date(2022, 12, 14), date(2023, 12, 15), 100)
addToBought("22", "test2", "name2", date(2023, 1, 22), date(2023, 6, 2), 50)

addToSold("1265", "12", date(2022, 12, 14), 14.50, 20)
addToSold("2223", "22",  date(2023, 1, 22), 16.50, 10)
dataList = getDataList("bought.csv")
searchList = ["12", "test", "name", "2022-12-14", "2023-12-15", "100"]

#print(dataList[1])
#print(searchList)
#print(dataList[1] == searchList)
#print(getRowIndex(dataList, searchList))



#print(getBoughtListByBoughtId("12"))
#print(getSoldListByBoughtId("12"))
#print(int(getBoughtListByBoughtId("12")[0][5]) - int(getSoldListByBoughtId("12")[0][4]))