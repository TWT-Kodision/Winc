from csvController import*
from functions import*

make_bought_file()
make_sold_file()
add_to_bought(12, "name", date(2022, 12, 14), 15, date(2023, 12, 15))
add_to_bought(22, "name2", date(2023, 1, 22), 16, date(2023, 1, 2))
add_to_bought(23, "name3", date(2023, 1, 23), 17, date(2023, 1, 3))
add_to_bought(24, "name4", date(2023, 1, 24), 18, date(2023, 2, 4))
add_to_bought(25, "name2", date(2023, 1, 25), 19, date(2023, 6, 5))
add_to_bought(26, "name6", date(2023, 1, 26), 11, date(2023, 2, 6))
add_to_bought(27, "name6", date(2023, 1, 27), 12, date(2023, 6, 7))
add_to_bought(28, "name8", date(2023, 1, 28), 13, date(2023, 6, 8))
add_to_bought(29, "name6", date(2023, 1, 29), 14, date(2023, 6, 9))

add_to_sold(1265, 12, date(2023, 2, 14), 24.50)
add_to_sold(1266, 23, date(2023, 2, 14), 24.50)
add_to_sold(2223, 22, date(2023, 3, 22), 26.50)
add_to_sold(2323, 24, date(2023, 2, 22), 27.50)
add_to_sold(2423, 27, date(2023, 3, 22), 23.50)

test_function = Functions()

def test_inventory_list():
    expected_list = [['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date'], ['23', 'name3', '2023-01-23', '17', '2023-01-03'], ['24', 'name4', '2023-01-24', '18', '2023-02-04'], ['25', 'name2', '2023-01-25', '19', '2023-06-05'], ['26', 'name6', '2023-01-26', '11', '2023-02-06'], ['28', 'name8', '2023-01-28', '13', '2023-06-08'], ['29', 'name6', '2023-01-29', '14', '2023-06-09']]
    assert (test_function.get_inventory_list() == expected_list), "not the right inventory list"
    
def test_product_detail():
    expected_output= [['26', 'name6', '2023-01-26', '11', '2023-02-06'], ['29', 'name6', '2023-01-29', '14', '2023-06-09']]
    product = "name6"
    assert (test_function.get_product_details(product) == expected_output), "output productdetails not as expected"

def test_get_products_date_range():
    begin_date = date(2023,1,1)
    end_date = date(2023,1,26)
    list = "bought"
    expected_list = [['22', 'name2', '2023-01-22', '16', '2023-01-02'], ['23', 'name3', '2023-01-23', '17', '2023-01-03'], ['24', 'name4', '2023-01-24', '18', '2023-02-04'], ['25', 'name2', '2023-01-25', '19', '2023-06-05'], ['26', 'name6', '2023-01-26', '11', '2023-02-06']]
    assert (test_function.get_products_date_range(begin_date, end_date, list) == expected_list), "output product range not valid"

def test_calculate_profit():
    start_date = date(2023,2,1)
    end_date = date(2023,2,26)
    expected_output = 26.5
    output = test_function.calculate_profit(start_date, end_date)
    assert (output == expected_output), "profit is not as expected."

print('1')
test_inventory_list()
print('2')
test_product_detail()
print('3')
test_calculate_profit()
print('4')
test_get_products_date_range()
print('5')
print('tests complete')