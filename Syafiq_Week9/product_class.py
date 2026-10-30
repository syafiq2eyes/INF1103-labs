class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
    
    def display_information(self):
        print(f"{self.__product_id} | {self.__name} | ${self.__price:.2f} | {self.__stock} in stock")

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity




