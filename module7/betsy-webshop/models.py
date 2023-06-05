import peewee

db = peewee.SqliteDatabase("testshop.db")


class Tags(peewee.Model):
    tag_name = peewee.CharField()

    class Meta:
        database = db

class Users(peewee.Model):
    name = peewee.CharField()
    address = peewee.CharField()
    billing_info = peewee.CharField()

    class Meta:
        database = db

class Products(peewee.Model):
    name = peewee.CharField()
    seller_id = peewee.ForeignKeyField(Users)
    description = peewee.CharField()
    tags = peewee.ManyToManyField(Tags)
    in_stock = peewee.IntegerField()
    price = peewee.DecimalField(decimal_places=2, auto_round=True, default=0)

    class Meta:
        database = db

class Transactions(peewee.Model):
    sold_to_user_id = peewee.ForeignKeyField(Users)
    transaction_date = peewee.DateField()
    product_id = peewee.ForeignKeyField(Products)
    quantity = peewee.IntegerField()

    class Meta:
        database = db

products_tags = Products.tags.get_through_model()