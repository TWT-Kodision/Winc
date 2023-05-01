import models
import peewee
from typing import List
from datetime import datetime

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    sorted_dishes = []
    for dish in models.Dish.select().order_by(models.Dish.price_in_cents):
        sorted_dishes.append(dish)
    return sorted_dishes[0]
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    ...

def vegetarian_dishes() -> List[models.Dish]:
    vegetarian_dishes = []   
    for dish in models.Dish.select(models.Dish):
        is_vegetarian = True
        for ingredient in dish.ingredients:
            if ingredient.is_vegetarian == False:
                is_vegetarian = False
                break
        if is_vegetarian:
            if dish.name not in vegetarian_dishes:
                vegetarian_dishes.append(dish)
    return vegetarian_dishes 

    """You'd like to know what vegetarian dishes are available
me)
    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    ...

def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    name_and_avg_rating= {}
    rating_sum = {}
    rating_count = {}

    for rating in models.Rating.select().join(models.Restaurant):

        if rating.restaurant.id in rating_sum.keys():
            rating_sum[rating.restaurant.id] += rating.rating
            rating_count[rating.restaurant.id] += 1
        else:
            rating_sum[rating.restaurant.id] = rating.rating
            rating_count[rating.restaurant.id] = 1

    for restaurant in rating_sum.keys():
        name_and_avg_rating[restaurant] = (rating_sum[restaurant]/rating_count[restaurant])

    highest_score = max(name_and_avg_rating)
    return models.Restaurant.select().where(models.Restaurant.id == highest_score)

def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    rating = models.Rating(restaurant = 1, rating = 3)
    rating.save()


def dinner_date_possible() -> List[models.Restaurant]:
    planned_time ='19:00:00'
    open_restaurants = models.Restaurant.select().where(models.Restaurant.opening_time < planned_time, models.Restaurant.closing_time > planned_time)
    
    for restaurant in open_restaurants:
        has_vegan = False
        possible_restaurants = []
        #print(restaurant.name)
        for dish in models.Dish.select().where(models.Dish.served_at == restaurant.id):
            #print(dish.name)
            vegan_dish = True
            for ingredient in dish.ingredients:
                #print(ingredient.name)
                #print(ingredient.is_vegan)
                if ingredient.is_vegan == False:
                    vegan_dish = False
                    break
            if vegan_dish:
               possible_restaurants.append(restaurant)
    #print(possible_restaurants)
    return possible_restaurants       


    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    ...


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    new_dish = models.Dish.create(name = 'mac and cheese', served_at = 3,  price_in_cents = 1500)
    cheese = models.Ingredient.get_or_create(name = 'cheese', is_vegetarian = True, is_vegan = False, is_glutenfree = True)
    macaroni = models.Ingredient.get_or_create(name = 'macaroni', is_vegetarian = True, is_vegan = True, is_glutenfree = False)
    milk = models.Ingredient.get_or_create(name = 'milk', is_vegetarian = True, is_vegan = False, is_glutenfree = True)
    
    new_dish.ingredients.add(models.Ingredient.select().where(models.Ingredient.name == 'cheese'))
    new_dish.ingredients.add(models.Ingredient.select().where(models.Ingredient.name == 'macaroni'))
    new_dish.ingredients.add(models.Ingredient.select().where(models.Ingredient.name == 'milk'))
    return new_dish