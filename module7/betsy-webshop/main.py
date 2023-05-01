__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"
import models
from datetime import date
import difflib
from peewee import *

def search(term):
    products = models.Products.select()
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
        print(close_match)
        for product in products:
            if product.name.casefold() == close_match:
                result.append(product)
            if close_match in product.description.casefold():
                result.append(product)
    return(result)

def list_user_products(user_id):
        products = models.Products.select().where(models.Products.seller_id == user_id)
        return products

def list_products_per_tag(tag_id):
        found_products = []
        for product in  models.Products.select(models.Products):
            for tag in product.tags:
                if tag.id == tag_id:
                    found_products.append(product)
        return found_products        

def add_product_to_catalog(product_name, user_id, product_description, product_tags, stock: int, price: int) -> models.Products:
    add_product = models.Products.create(name = product_name, seller_id = user_id, description = product_description, in_stock = stock)   
    add_price = models.Prices.create(product_id = add_product.id, price_in_cents = price)
    #split tags, split with space
    splitted_tags = product_tags.split()
    #add tags to model
    for tag in splitted_tags:
        tag_lower = tag.lower()
        new_tag = models.Tags.get_or_create(tag_name = tag_lower)
        add_product.tags.add(models.Tags.get(models.Tags.tag_name == tag_lower))

def update_stock(product_id, new_quantity):
    product = models.Products.get(models.Products.id == product_id)
    product.in_stock = new_quantity
    product.save()

def purchase_product(product_id, buyer_id, quantity, date = date.today()):
    product = models.Products.get(models.Products.id == product_id)
    if (product.in_stock >= quantity): 
        new_transaction = models.Transactions.create(sold_to_user_id = buyer_id, product_id = product_id, quantity = quantity, transaction_date = date)
        #update stock
        new_quantity = product.in_stock - quantity
        update_stock(product_id, new_quantity)
    else:
        print('not enough in stock')

def remove_product(product_id):
    product = models.Products.get(models.Products.id == product_id)
    price = models.Price.get(models.Prices.product_id == product_id)
    product.delete_instance()
    price.delete_instance()

def populate_test_database(add_users = True, add_products = True, add_transactions = True, update_stocks = True):
    
    db = SqliteDatabase("testshop.db")
    db.create_tables([models.Tags, models.Products, models.Users, models.Prices, models.Transactions, models.products_tags])

    if(add_users): 
        userbob = models.Users.create(name = "Bob", address = "Thisstreet 5, 1234ab , place", billing_info = "this is billing info of Bob")
        useralice = models.Users.create(name = "Alice", address = "Thatstreet 32, 4321BA , secondplace", billing_info = "this is billing info of Alice")
        userkodi = models.Users.create(name = "Kodi", address = "Anotherstreet 75, 9876QW , thirdplace", billing_info = "this is billing info of Kodi")

    if(add_products):
        add_product_to_catalog("jeans",1 , "blue jeans", "blue jeans men", 3, 3000)
        add_product_to_catalog("t-shirt",1 , "white t-shirt size:m", "t-shirt white unisex", 2, 1000 )
        add_product_to_catalog("socks",2 , "black socks size 45", "black socks", 5, 500)
        add_product_to_catalog("sweater",3 , "green sweater", "green sweater size:m", 2, 5000)
        add_product_to_catalog("T-shirt",3 , "grey color t-shirt size:m", "grey t-shirt unisex", 2, 1200)
        add_product_to_catalog("jeans", 3, "white jeans", "White Jeans women", 6, 4000)

    if(add_transactions): #(product_id, buyer_id, date)
        purchase_product(1,1,3)
    
    if(update_stocks):
        update_stock(5,6)

populate_test_database()
print(search('whie'))
print(search('size'))