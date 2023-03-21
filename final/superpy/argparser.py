import argparse
from functions import*


parser = argparse.ArgumentParser(description='Inventory administration')
function_selector = parser.add_subparsers(dest = 'function')

inventory_list = function_selector.add_parser('inventory_list', help = 'shows the complete list of the current inventory')

product_details = function_selector.add_parser('product_detail', help = 'shows the details of a product')
product_details.add_argument('-product_name', help = 'name of product to show the details', type = str)

expired_list = function_selector.add_parser('expired_list', help = 'shows the list of expired products in inventory')

product_date = function_selector.add_parser('date_range', help = 'shows the list of bought or sold products in a given date range')
product_date.add_argument('-start_date', help = 'give the starting date YYYY-MM-DD of the range', type = datetime)
product_date.add_argument('-end_date', help = 'give the ending date of the range YYYY-MM-DD', type = datetime)
product_date.add_argument('-bought_sold', help = 'for sold list type "s" for bought list type "b"', type = str)

profit = function_selector.add_parser('profit', help = 'calculates the profit in a given date range')
profit.add_argument('-start_date', help = 'give the starting date YYYY-MM-DD of the range', type = datetime)
profit.add_argument('-end_date', help = 'give the ending date of the range YYYY-MM-DD', type = datetime)

inventory_count = function_selector.add_parser('inventory_count', help = 'counts the amount of each product in the inventory')

sold_graph = function_selector.add_parser('plot_sold_graph', help = 'plots a sold per day graph in given date range')
sold_graph.add_argument('-start_date', help = 'give the starting date YYYY-MM-DD of the range', type = datetime)
sold_graph.add_argument('-end_date', help = 'give the ending date of the range YYYY-MM-DD', type = datetime)


args = parser.parse_args()

if args.function == 'inventory_list':
    print(get_inventory_list())
if args.function == 'product_detail':
    print(get_product_details(args.product_name))
if args.function == 'expired_list':
    print(get_expired_product_list())
if args.function == 'date_range':
    print(get_products_date_range(args.start_date, args.end_date, args.bought_sold))
if args.function == 'profit':
    print(calculate_profit(args.start_date, args.end_date))
if args.function == 'inventory_count':
    print(count_each_product_inventory())
if args.function == 'plot_sold_graph':
    print(make_date_sold_graph(args.start_date, args.end_date))

#todo 
#date checker
#classes
#testscript
#add product bought/sold list
#put generated list in csv file  


#python argparser.py inventory_list -h  
#python argparser.py product_detail -product_name name6