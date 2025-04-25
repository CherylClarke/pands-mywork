# messing with dictionaries

car = {
    "make" : "ford",
    "model" : "modeo",
    "year" : "2006",
    "owner" : {
        "name" : "andrew",
        "driver-number" : 1234
    }
}
'''
print (car)
'''
attr = "make"
print (car[attr])


print(car["year"])
print(car["owner"]["name"])
print (type(car["owner"].get("name")))