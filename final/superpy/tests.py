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
#dataList = getDataList("bought.csv")
#searchList = ["12", "test", "name", "2022-12-14", "2023-12-15"]

#print(dataList[1])
#print(searchList)
#print(getDataList("bought.csv"))
#print(getDataList("sold.csv"))
#print(dataList[1] == searchList)
#print(getRowIndex(dataList, searchList))




#print(getBoughtListByBoughtId("12"))
#print(getSoldListByBoughtId("12"))
#print(int(getBoughtListByBoughtId("12")[0][5]) - int(getSoldListByBoughtId("12")[0][4]))



#print('list is')
print(get_inventory_list())
#print(getProductDetails("name2"))
#print(get_expired_product_list())
#print(calculate_profit("2023-02-01", "2023-2-28"))
#print(count_each_product_inventory())
#print(make_date_array("2023-02-01", "2023-2-28"))
#print(count_sold_products_per_day('2023-03-22'))
#make_date_sold_graph("2023-02-01", "2023-2-28")
make_custom_file("custom.csv", get_inventory_list())