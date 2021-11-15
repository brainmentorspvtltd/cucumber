products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"leather jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]

toSearch = input("Search Here... : ")
toSearch = toSearch.lower()

searchResults = []

for i in range(len(products)):
    p_name = products[i]["p_name"].lower()
    brand = products[i]["brand"].lower()
    category = products[i]["Category"].lower()

    # if toSearch == p_name or toSearch == brand or toSearch == category:
    # if p_name.find(toSearch) != -1 or brand.find(toSearch) != -1 or category.find(toSearch) != -1:
    if toSearch in p_name or toSearch in brand or toSearch in category:
        print("Product Name :",p_name.title())
        print("Product Price :",products[i]["price"])
        print("Product Brand :",brand.title())
        print("Product Category :",category.title())
        print("*" * 20)
        searchResults.append(products[i])

def func(x):
    return x["price"]

option = input("Do you want to filter data based on price [yes/no] : ").lower()
if option == "yes" or option == "y":
    print("""
    1. Low to High
    2. High to Low
    """)
    order = input("Choose the order : ")
    if order == "1":
        data = sorted(searchResults, key=func)
        print(data)
    else:
        data = sorted(searchResults, key=func, reverse=True)
        print(data)




