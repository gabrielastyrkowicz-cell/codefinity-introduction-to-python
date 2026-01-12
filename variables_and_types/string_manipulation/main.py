grocery_items = "milk cheese bread apples oranges chicken"

dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]
fruit1 = grocery_items[18:24]
fruit2 = grocery_items[25:32]
meat1 = grocery_items[-7:]
aisle = "5"

message = "We have items:" + " " + dairy1 + ", " + dairy2  + ", " +  bakery1 + ", " + fruit1 + ", " + fruit2 + ", " + meat1 + " in aisle " + aisle + "."
print(message)