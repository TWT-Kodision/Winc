from peewee import *
import models
import os
from datetime import date


#switches
add_users = True
add_products = True
add_transactions = True


#create DB
db = SqliteDatabase("testshop.db")
db.create_tables([models.Tags, models.Products, models.Users, models.Prices, models.Transactions, models.products_tags])


def split_tags(tags):
    tag_list = tags.split()
    return tag_list

def add_product(product_name, user_id: int, product_description, product_tags, stock: int, price: int) -> models.Products:
    add_product = models.Products.create(name = product_name, seller_id = user_id, description = product_description, in_stock = stock)   
    add_price = models.Prices.create(product_id = add_product.id, price_in_cents = price)
    #add tags, split with space:
    for tag in split_tags(product_tags):
        new_tag = models.Tags.get_or_create(tag_name = tag)
        add_product.tags.add(models.Tags.get(models.Tags.tag_name == tag))

def add_transaction(product_id, buyer_id, quantity, date = date.today()):
    new_transaction = models.Transactions.create(sold_to_user_id = buyer_id, product_id = product_id, quantity = quantity, transaction_date = date)

if(add_users): 
    userbob = models.Users.create(name = "Bob", address = "Thisstreet 5, 1234ab , place", billing_info = "this is billing info of Bob")
    useralice = models.Users.create(name = "Alice", address = "Thatstreet 32, 4321BA , secondplace", billing_info = "this is billing info of Alice")
    userkodi = models.Users.create(name = "Kodi", address = "Anotherstreet 75, 9876QW , thirdplace", billing_info = "this is billing info of Kodi")

if(add_products):
    add_product("jeans",1 , "blue jeans", "blue jeans men", 3, 3000)
    add_product("t-shirt",1 , "white t-shirt size:m", "t-shirt white unisex", 2, 1000 )
    add_product("socks",2 , "black socks size 45", "black socks", 5, 500)
    add_product("sweater",3 , "green sweater", "green sweater size:m", 2, 5000)
    add_product("T-shirt",3 , "grey color t-shirt size:m", "grey t-shirt unisex", 2, 1200)

if(add_transactions): #(product_id, buyer_id, date)
    add_transaction(1,1,3)






