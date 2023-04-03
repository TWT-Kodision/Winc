import argparse
from functions import Functions

class Command:
    parser = argparse.ArgumentParser(description='Inventory administration')
    function_selector = parser.add_subparsers(dest = 'function')
    #option get inventory list
    inventory_list = function_selector.add_parser('inventory_list', help = 'shows the complete list of the current inventory')
    inventory_list.add_argument('--file_name', help = 'optional: to export list to csv file, give the filename', type = str)
    #option get product_detail
    product_details = function_selector.add_parser('product_detail', help = 'shows the details of a product')
    product_details.add_argument('-product_name', help = 'name of product to show the details', type = str)
    #option get xpired_list
    expired_list = function_selector.add_parser('expired_list', help = 'shows the list of expired products in inventory')
    expired_list.add_argument('--file_name', help = 'optional: to export list to csv file, give the filename', type = str)
    #option get product list by date range
    product_date = function_selector.add_parser('date_range', help = 'shows the list of bought or sold products in a given date range')
    product_date.add_argument('-start_date', help = 'give the starting date YYYY-MM-DD of the range', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    product_date.add_argument('-end_date', help = 'give the ending date of the range YYYY-MM-DD', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    product_date.add_argument('-bought_sold', help = 'for sold list type "s" for bought list type "b"', type = str)
    product_date.add_argument('--file_name', help = 'optional: to export list to csv file, give the filename', type = str)
    #option calculate profit
    profit = function_selector.add_parser('profit', help = 'calculates the profit in a given date range')
    profit.add_argument('-start_date', help = 'give the starting date YYYY-MM-DD of the range', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    profit.add_argument('-end_date', help = 'give the ending date of the range YYYY-MM-DD', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    #option count inventory
    inventory_count = function_selector.add_parser('inventory_count', help = 'counts the amount of each product in the inventory')
    #option plot sold graph
    sold_graph = function_selector.add_parser('plot_sold_graph', help = 'plots a sold per day graph in given date range')
    sold_graph.add_argument('-start_date', help = 'give the starting date YYYY-MM-DD of the range', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    sold_graph.add_argument('-end_date', help = 'give the ending date of the range YYYY-MM-DD', type = lambda t: datetime.strptime(t, '%Y-%m-%d').date())
    #option add to bought list
    add_bought_list = function_selector.add_parser('add_bought', help = 'add a product to bought list')
    add_bought_list.add_argument('-id', help = 'give the id number', type = int)
    add_bought_list.add_argument('-name', help = 'give the name of the product', type = str)
    add_bought_list.add_argument('-buy_date', help = 'give the bought date of the product YYYY-MM-DD', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    add_bought_list.add_argument('-buy_price', help = 'give the bought price of the product', type = float)
    add_bought_list.add_argument('-expiration_date', help = 'give the expiration date in YYYY-MM-DD', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    #option add to sold list
    add_sold_list = function_selector.add_parser('add_sold', help = 'add a product to sold list')
    add_sold_list.add_argument('-id', help = 'give the id number', type = int)
    add_sold_list.add_argument('-bought_id', help = 'give the bought id of the product', type = int)
    add_sold_list.add_argument('-sell_date', help = 'give the sell date of the product YYYY-MM-DD', type = lambda s: datetime.strptime(s, '%Y-%m-%d').date())
    add_sold_list.add_argument('-sell_price', help = 'give the bought price of the product', type = float)


    #options switch
    def switch(self):
        call_function = Functions()
        args = self.parser.parse_args()
        if args.function == 'inventory_list':
            result = call_function.get_inventory_list()
            call_function.print_list(result)
        if args.function == 'product_detail':
            print(call_function.get_product_details(args.product_name))
        if args.function == 'expired_list':
            result = call_function.get_expired_product_list()
            call_function.print_list(result)
        if args.function == 'date_range':
            result = call_function.get_products_date_range(args.start_date, args.end_date, args.bought_sold)
            call_function.print_list(result)
        if args.function == 'profit':
            print(call_function.calculate_profit(args.start_date, args.end_date))
        if args.function == 'inventory_count':
            print(call_function.count_each_product_inventory())
        if args.function == 'plot_sold_graph':
            call_function.make_date_sold_graph(args.start_date, args.end_date)
        if args.function == 'add_bought':
            call_function.register_bought_product(args.id, args.name, args.buy_date, args.buy_price, args.expiration_date)
            print("product added to bought list")
        if args.function == 'add_sold':
            call_function.register_sold_product(args.id, args.bought_id, args.sell_date, args.sell_price)
            print("product added to sold list")

        try: 
            if args.file_name is not None:
                make_custom_file(args.file_name, result, content = args.function)
        except AttributeError:
            pass

