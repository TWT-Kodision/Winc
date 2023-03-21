from csvController import*
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

#===============================
#Utils

def convert_to_date_object(date):
    date_object = datetime.strptime(date, '%Y-%m-%d').date()
    return date_object

def make_date_array(start_date, end_date):
    begin_date_object = convert_to_date_object(start_date)
    end_date_object = convert_to_date_object(end_date)
    date_array = []
    while begin_date_object <= end_date_object:
        date_array.append(str(begin_date_object))
        begin_date_object += timedelta(days=1)
    return date_array

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

def validate_date(date):
    format = "%d-%m-%Y"
    res = True
    try:
        res = bool(datetime.strptime(date, format))
    except ValueError:
        res = False
    return res 

#===============================
def make_new_csv_file(filename, column_name=None):
    try:
        if filename == "bought.csv":
            make_bough_file()
        elif filename == "sold.csv":
            make_sold_file()
        else:
            make_file(filename, column_name)
    except ValueError:
        print("filename or column name not correct")

def register_bought_product(id, product, product_name, buy_date, expiration_date):
    add_to_bought(id, product, product_name, buy_date, expiration_date)

def register_sold_product(id, bought_id, sell_date, sell_price):
    add_to_sold(id, bought_id, sell_date, sell_price)

def get_inventory_list():
    sold_list = get_data_list("sold.csv")
    inventory_list = get_data_list("bought.csv")
    for sold_item in sold_list:
        for bought_item in inventory_list:
            if sold_item[1] == bought_item [0]:
                sold_list.remove(sold_item)
                inventory_list.remove(bought_item)
    return inventory_list

def get_product_details(search_product):
    inventory_list = get_inventory_list()
    product_details = []
    for product in inventory_list:
        if product[1] == search_product:
            product_details.append(product)
    return product_details

def get_expired_product_list(day = date.today()):
    inventory_list = get_inventory_list()
    del inventory_list[0] #remove header
    expired_products = []
    for product in inventory_list:
        date_object = convert_to_date_object(product[4])
        if (date_object) <= day:
            expired_products.append(product)
    return expired_products

def get_sold_product_list():
    sold_products = get_data_list("sold.csv")
    return sold_products

def find_product_by_id(id):
    bought_list = get_data_list("bought.csv")
    for product in bought_list:
        if product[0]==id:
            return product
        
def get_products_date_range(begin_date, end_date, bought_or_sold):
    begin_date_object = convert_to_date_object(begin_date)
    end_date_object = convert_to_date_object(end_date)
    list_range = []
    if bought_or_sold == "bought":
        product_list = get_data_list("bough.csv")
    if bought_or_sold == "sold":
        product_list = get_data_list("sold.csv")
    del product_list[0] #remove header
    for product in product_list:
        product_date_object = convert_to_date_object(product[2])
        if product_date_object >= begin_date_object and product_date_object <= end_date_object:
            list_range.append(product)
    return list_range

def calculate_profit(begin_date, end_date):
    #make sold list for specified range
    sold_list_range = get_products_date_range(begin_date, end_date, "sold")
    profit = 0
    for product in sold_list_range:
        print(product)
        product_bought_details = find_product_by_id(product[1])
        print(product_bought_details)
        product_profit =  float(product[3])-float(product_bought_details[3])
        profit += product_profit
    return profit  

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

def count_sold_products_per_day(date):
    sold_products = get_sold_product_list()
    count = 0
    for product in sold_products:
        if product[2] == date:
            count += 1
    return count

def make_dict_day_count(start_date, end_date):
    dates = make_date_array(start_date, end_date)
    sold_on_dates = {}
    for date in dates:
        sold_on_dates[date] = count_sold_products_per_day(str(date))
    return sold_on_dates

def make_date_sold_graph(start_date, end_date):
    dates_sold = make_dict_day_count(start_date, end_date)
    create_graph(dates_sold)




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
