from csvController import*
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

#===============================
#Utils
#convert date string to date object
def convert_to_date_object(date):
    date_object = datetime.strptime(date, '%Y-%m-%d').date()
    return date_object

#using begin and end date, it makes an array with al days in between. 
def make_date_array(start_date, end_date):
    date_array = []
    while start_date <= end_date:
        date_array.append(str(start_date))
        start_date += timedelta(days=1)
    return date_array

#plots graph
def create_graph(axis):
    x=[]
    y=[]
    for key in axis.keys():
        x.append(key)
    for value in axis.values():
        y.append(value)
    new_list = range(min(y), max(y))
    plt.yticks(new_list)
    plt.xticks(rotation=90)
    x_axis = np.array(x)
    y_axis = np.array(y)
    plt.plot(x_axis, y_axis)
    plt.show()

#print list with the items among eacht other
def print_list(list):
    for item in list: 
        print(item)

#===============================

#makes new csv file 
def make_new_csv_file(filename, column_name=None):
    try:
        if filename == "bought.csv":
            make_bought_file()
        elif filename == "sold.csv":
            make_sold_file()
        else:
            make_file(filename + ".csv", column_name)
    except ValueError:
        print("filename or column name not correct")

#ads bought product
def register_bought_product(id, product, product_name, buy_date, expiration_date):
    add_to_bought(id, product, product_name, buy_date, expiration_date)

#adrs sold product
def register_sold_product(id, bought_id, sell_date, sell_price):
    add_to_sold(id, bought_id, sell_date, sell_price)

#makes inventory list per product
def get_inventory_list():
    sold_list = get_data_list("sold.csv")
    inventory_list = get_data_list("bought.csv")
    for sold_item in sold_list:
        for bought_item in inventory_list:
            if sold_item[1] == bought_item [0]:
                sold_list.remove(sold_item)
                inventory_list.remove(bought_item)
    return inventory_list

#gets product details from product in inventory list
def get_product_details(product_name):
    inventory_list = get_inventory_list()
    product_details = []
    for product in inventory_list:
        if product[1] == product_name:
            product_details.append(product)
    return product_details


#gets list of expired prooducts (in stock)
def get_expired_product_list(day = date.today()):
    inventory_list = get_inventory_list()
    del inventory_list[0] #remove header
    expired_products = []
    for product in inventory_list:
        date_object = convert_to_date_object(product[4])
        if (date_object) <= day:
            expired_products.append(product)
    return expired_products

#get sold list
def get_sold_product_list():
    sold_products = get_data_list("sold.csv")
    return sold_products

#get bought list
def find_product_by_id(id):
    bought_list = get_data_list("bought.csv")
    for product in bought_list:
        if product[0]==id:
            return product
        
#find product in a given date range        
def get_products_date_range(begin_date, end_date, bought_or_sold):
    begin_date 
    end_date 
    list_range = []
    if bought_or_sold == "bought":
        product_list = get_data_list("bought.csv")
    if bought_or_sold == "sold":
        product_list = get_data_list("sold.csv")
    del product_list[0] #remove header
    for product in product_list:
        product_date_object = convert_to_date_object(product[2])
        if product_date_object >= begin_date and product_date_object <= end_date:
            list_range.append(product)
    return list_range

#calculate profit in a given date range the products are sold
def calculate_profit(begin_date, end_date):
    #make sold list for specified range
    sold_list_range = get_products_date_range(begin_date, end_date, "sold")
    profit = 0
    for product in sold_list_range:
        product_bought_details = find_product_by_id(product[1])
        product_profit =  float(product[3])-float(product_bought_details[3])
        profit += product_profit
    return profit  

#gives a dictionary with each product and the count of it that is currently on stock
def count_each_product_inventory():
    inventory_list = get_inventory_list()
    counts = dict()
    del inventory_list[0]
    for product in inventory_list:
        counter = 0
        for compare_product in inventory_list:
            if product[1]==compare_product[1]:
                counter += 1
        counts[product[1]] = counter
    return(counts)

#coutn products on a given date
def count_sold_products_per_day(date):
    sold_products = get_sold_product_list()
    count = 0
    for product in sold_products:
        if product[2] == date:
            count += 1
    return count

#create dictionary with the product count on each dat given the date range. This is used to plot the graph
def make_dict_day_count(start_date, end_date):
    dates = make_date_array(start_date, end_date)
    sold_on_dates = {}
    for date in dates:
        sold_on_dates[date] = count_sold_products_per_day(str(date))
    return sold_on_dates

#create graph of number of sold products per day
def make_date_sold_graph(start_date, end_date):
    dates_sold = make_dict_day_count(start_date, end_date)
    create_graph(dates_sold)

#puts list in a csv file.
def make_custom_file(filename, list, content = "custom file"):
    make_new_csv_file(filename, [content])
    add_to_file(filename +".csv", list)
    
