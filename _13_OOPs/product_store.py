# Design and create an online store for products (name, price).
# Track total products bieng created.
# Create a static method to calculate discount on each product based on a% parameter


class product:
    count = 0 # common for all objects so it should be inside a class variable/attribute
    
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        product.count += 1    #A) to know about the creation of new  objects, we need to put it in the constructor
                              #                         'product' cause we are making count under 'product class'
                              #B) instead if we use 'self.count'  a new variable will be formed with the name 'count' wchich will only
                              #                       access the 'instances' not the 'class' so to count both we used 'product.count'
   
    def get_info(self): # instance method
        print(f"The price of {self.product_name}is Rs. {self.price}")

    @staticmethod
    def cal_discount( price, a):
        final_price = price - (a * price / 100)
        print(f"discounted price is = {final_price}")  
    
    @classmethod
    def get_count(cls):
        print(f"Total products = {cls.count}")

p1 = product("Phone", 12000)
p2 = product("Laptop", 55000)
p3 = product("TV", 25000)



product.get_count()   # discounted price is = 10560.0
p1.cal_discount(p1.price, 12)   # discounted price is = 10560.0


