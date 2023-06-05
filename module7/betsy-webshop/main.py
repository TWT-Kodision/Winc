__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"
import models
from datetime import date
import difflib
from peewee import *

# prints the products in the objects ;
def print_products(product_object):
    for product in product_object:
        formatted_price = "{:.2f}".format(product.price)
        print("id: "+str(product.id)+ " product name: "+ product.name+", description: "+product.description+", price: "+formatted_price)

#checks if the given username exists. 
def username_exists(username):
    query = models.Users.select().where(models.Users.name == username)
    return query.exists()

#checks if the product id excists
def product_exists(product_id):
    products = models.Products.select()
    exists = False
    for product in products:
        if product.id == product_id:
            exists = True
    return exists
    
def get_user_id(username):
    if username_exists(username):
        query =  models.Users.select().where(models.Users.name == username)
        for user in query:
            return user
    else:
        print('user does not exist')

#prints products list with products that has the search term in the description or procctname 
def search(term):
    products = models.Products.select() #indexing
    result = []
    possibilities = []
        #fill possibilities with tags and words from description
    for tags in models.Tags.select():
        possibilities.append(tags.tag_name.casefold())
    for product in products:
        description_splitted = product.description.split()
        for word in description_splitted:
            possibilities.append(word.casefold())
    #find possible word
    close_matches = difflib.get_close_matches(term.casefold(), possibilities, 2) 
    for close_match in close_matches:
        for product in products:
            if product.name.casefold() == close_match and product not in result: #check if its a new match in product name
                result.append(product)
            if close_match in product.description.casefold() and product not in result: #check if its a new match in description
                result.append(product)
    if result:
        print_products(result)
    else:
        print('no results')

def list_user_products(user_name):
    if username_exists(user_name):
        users = models.Users.select().where(models.Users.name == user_name)
        for user in users:
            products = models.Products.select().where(models.Products.seller_id == user.id)
            print_products(products)
    else: 
        print('username does not exists')

def list_products_per_tag(tag_name):
    found_products = []
    for product in  models.Products.select(models.Products):
        for tag in product.tags:
            if tag.tag_name == tag_name:
                found_products.append(product)
    if found_products:
        print_products(found_products)
    else:    
        print('no products found')    

def add_product_to_catalog(product_name: str, user_id: int, product_description: str, product_tags: int, stock: int, price: float) -> models.Products:
    try:
        add_product = models.Products.create(name = product_name, seller_id = user_id, description = product_description, in_stock = stock, price = price)   
        #split tags, split with space
        splitted_tags = product_tags.split()
        #add tags to model
        for tag in splitted_tags:
            tag_lower = tag.lower()
            models.Tags.get_or_create(tag_name = tag_lower) #creates new tag if it doesnt exist already, otherwise it gets the tag_id. 
            add_product.tags.add(models.Tags.get(models.Tags.tag_name == tag_lower))
    except:
        print('an error accured, check the input')

def update_stock(product_id, new_quantity):
    if product_exists(product_id):
        product = models.Products.get(models.Products.id == product_id)
        product.in_stock = new_quantity
        product.save()
    else:
        print('product not found')

def purchase_product(product_id, buyer_name, quantity, date = date.today()):
    if username_exists(buyer_name) and product_exists(product_id):
        product = models.Products.get(models.Products.id == product_id)
        buyer_id = get_user_id(buyer_name)
        if (product.in_stock >= quantity): 
            models.Transactions.create(sold_to_user_id = buyer_id, product_id = product_id, quantity = quantity, transaction_date = date)
            #update stock
            new_quantity = product.in_stock - quantity
            update_stock(product_id, new_quantity)
        else:
            print('not enough in stock')
    else:
        print('buyer name or product id does not exist')

def remove_product(product_id):
    if product_exists(product_id):
        product = models.Products.get(models.Products.id == product_id)
        price = models.Prices.get(models.Prices.product_id == product_id)
        product.delete_instance()
        price.delete_instance()
    else:
        print('product does not exist')

def add_user(name, address, billing_info):
    if username_exists(name):
        print('username already exists')
    else:
        models.Users.create(name = name, address = address, billing_info = billing_info)

def populate_test_database(add_users = True, add_products = True, add_transactions = True, update_stocks = True):
    
    db = SqliteDatabase("testshop.db")
    db.create_tables([models.Tags, models.Products, models.Users, models.Transactions, models.products_tags])

    if(add_users): 
        add_user(name = "Bob", address = "Thisstreet 5, 1234ab , place", billing_info = "this is billing info of Bob")
        add_user(name = "Alice", address = "Thatstreet 32, 4321BA , secondplace", billing_info = "this is billing info of Alice")
        add_user(name = "Kodi", address = "Anotherstreet 75, 9876QW , thirdplace", billing_info = "this is billing info of Kodi")

    if(add_products):
        add_product_to_catalog("jeans",1 , "blue jeans", "blue jeans men", 3, 30.55856)
        add_product_to_catalog("t-shirt",1 , "white t-shirt size:m", "t-shirt white unisex", 2, 10.10 )
        add_product_to_catalog("socks",2 , "black socks size 45", "black socks", 5, 5.00)
        add_product_to_catalog("sweater",3 , "green sweater", "green sweater size:m", 2, 50.00)
        add_product_to_catalog("T-shirt",3 , "grey color t-shirt size:m", "grey t-shirt unisex", 2, 12.00)
        add_product_to_catalog("jeans", 3, "white jeans", "White Jeans women", 6, 40.00)

    if(add_transactions): #(product_id, buyer_name, quantity, optional: date)
        purchase_product(1,1,3)
    
    if(update_stocks):
        update_stock(5,6)

if __name__ == "__main__":
    #populate_test_database(True, True, False, False)
    #search('whie')
    search('whiesdfsdfgsdfg')
    search('size')
    #list_user_products("Alice")
    #list_products_per_tag("white")
    #update_stock(1, 6)
    #add_user(name = "Bob", address = "Thisstreet 5, 1234ab , place", billing_info = "this is billing info of Bob")
    #get_user_id('Alice')
    #purchase_product(1,'Alice',2)
    #purchase_product(1,'alice',2)
    #emove_product(5)
    #print(product_exists(1))