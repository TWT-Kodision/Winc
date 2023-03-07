from csvController import*
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np

#===============================
#Utils

def convertToDateObject(date):
    date_object = datetime.strptime(date, '%Y-%m-%d').date()
    return date_object

def makeDateArray(begin_date, end_date):
    begin_date_object = convertToDateObject(begin_date)
    end_date_object = convertToDateObject(end_date)
    date_array = []
    while begin_date_object <= end_date_object:
        date_array.append(str(begin_date_object))
        begin_date_object += timedelta(days=1)
    return date_array

#===============================
def makeNewCSVFile(filename, column_name=None):
    try:
        if filename == "bought.csv":
            makeBoughtFile()
        elif filename == "sold.csv":
            makeSoldFile()
        else:
            makeFile(filename, column_name)
    except ValueError:
        print("filename or column name not correct")

def checkProductInput(inputList):
    return None

def registerBoughtProduct(id, product, product_name, buy_date, expiration_date):
    addToBought(id, product, product_name, buy_date, expiration_date)

def registerSoldProduct(id, bought_id, sell_date, sell_price):
    addToSold(id, bought_id, sell_date, sell_price)

def inventoryList():
    sold_list = getDataList("sold.csv")
    inventory_list = getDataList("bought.csv")
    for sold_item in sold_list:
        for bought_item in inventory_list:
            if sold_item[1] == bought_item [0]:
                sold_list.remove(sold_item)
                inventory_list.remove(bought_item)
    return inventory_list

def getProductDetails(search_product):
    inventory_list = inventoryList()
    product_details = []
    for product in inventory_list:
        if product[1] == search_product:
            product_details.append(product)
    return product_details

def getExpiredProductList(day = date.today()):
    inventory_list = inventoryList()
    del inventory_list[0] #remove header
    expired_products = []
    for product in inventory_list:
        date_object = convertToDateObject(product[4])
        if (date_object) <= day:
            expired_products.append(product)
    return expired_products

def getSoldProductList():
    sold_products = []
    return sold_products

def findProductById(id):
    bought_list = getDataList("bought.csv")
    for product in bought_list:
        if product[0]==id:
            return product
        
def getProductsDateRange(begin_date, end_date, bought_or_sold):
    begin_date_object = convertToDateObject(begin_date)
    end_date_object = convertToDateObject(end_date)
    list_range = []
    if bought_or_sold == "bought":
        product_list = getDataList("bough.csv")
    if bought_or_sold == "sold":
        product_list = getDataList("sold.csv")
    del product_list[0] #remove header
    for product in product_list:
        product_date_object = convertToDateObject(product[2])
        if product_date_object >= begin_date_object and product_date_object <= end_date_object:
            list_range.append(product)
    return list_range

def calculateProfit(begin_date, end_date):
    #make sold list for specified range
    sold_list_range = getProductsDateRange(begin_date, end_date, "sold")
    profit = 0
    for product in sold_list_range:
        print(product)
        product_bought_details = findProductById(product[1])
        print(product_bought_details)
        product_profit =  float(product[3])-float(product_bought_details[3])
        profit += product_profit
    return profit  

def countEachProductInventory():
    inventory_list = inventoryList()
    counts = dict()
    del inventory_list[0]
    for product in inventory_list:
        counter = 0
        for compare_product in inventory_list:
            if product[1]==compare_product[1]:
                counter += 1
        counts[product[1]] = counter
    return(counts)


#def plotGraphSoldProducts(begin_date, end_date):


#product list
#product list with number/count
#product bought price and expiry date
#product sold price
#expired products
#set date to today or future date
#list of bought and sold products at certain date
#profit time for specific time period
#export selection data to csv file 


""" Which products the supermarket offers;
    How many of each type of product the supermarket holds currently;
    How much each product was bought for, and what its expiry date is;
    How much each product was sold for or if it expired, the fact that it did;
    
    Setting and advancing the date that the application perceives as 'today';
    Recording the buying and selling of products on certain dates;
    Reporting revenue and profit over specified time periods;
    Exporting selections of data to CSV files;
    Two other additional non-trivial features of your choice, for example:
        The use of an external module Rich(opens in a new tab) to improve the application.
        The ability to import/export reports from/to formats other than CSV (in addition to CSV)
        The ability to visualize some statistics using Matplotlib(opens in a new tab)
        Another feature that you thought of.  
        """
